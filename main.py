import os
import random
import time
import cloud_genshin
import config
import hoyo_checkin
import login
import mihoyobbs
import push
import setting
import gamecheckin
import tools
from error import *
from loghelper import log


def checkin_game(game_name, game_module, game_print_name=""):
    if config.config["games"]["cn"][game_name]["auto_checkin"]:
        time.sleep(random.randint(2, 8))
        if game_print_name == "":
            game_print_name = game_name
        log.info(f"正在进行{game_print_name}签到")
        return_data = f"\n\n{game_module().sign_account()}"
        return return_data
    return ""


def main():
    # 拒绝在GitHub Action运行
    if os.getenv('GITHUB_ACTIONS') == 'true':
        print("请不要在GitHub Action运行本项目")
        exit(0)
    # 初始化，加载配置
    return_data = "\n"
    config.load_config()
    if not config.config["enable"]:
        log.warning("Config未启用！")
        return 1, "Config未启用！"
    elif config.config["account"]["cookie"] == "CookieError":
        raise CookieError('Cookie expires')
    # 检测参数是否齐全，如果缺少就进行登入操作，同时判断是否开启开启米游社签到
    if (config.config["account"]["stuid"] == "" or config.config["account"]["stoken"] == "") and \
            (config.config["mihoyobbs"]["enable"] or config.config['games']['cn']["enable"]):
        # 登入，如果没开启bbs全局没打开就无需进行登入操作
        if config.config["mihoyobbs"]["enable"]:
            login.login()
            time.sleep(random.randint(2, 8))
        # 整理 cookie，在字段重复时优先使用最后出现的值
        config.config["account"]["cookie"] = tools.tidy_cookie(config.config["account"]["cookie"])
    # 米游社签到
    ret_code = 0
    if config.config["mihoyobbs"]["enable"]:
        # 获取要使用的BBS列表,#判断是否开启bbs_Signin_multi
        if config.config["mihoyobbs"]["checkin_multi"]:
            setting.mihoyobbs_List_Use = [
                setting.mihoyobbs_List.get(i) for i in config.config["mihoyobbs"]["checkin_multi_list"]
                if setting.mihoyobbs_List.get(i) is not None]

        else:
            # 关闭bbs_Signin_multi后只签到大别墅
            setting.mihoyobbs_List_Use = [setting.mihoyobbs_List.get("id")]
        print(setting.mihoyobbs_List_Use)
        bbs = mihoyobbs.Mihoyobbs()
        return_data += bbs.run_task()
    # 国服
    if config.config['games']['cn']["enable"]:
        # 崩坏2签到
        return_data += checkin_game("honkai2", gamecheckin.Honkai2, "崩坏学园2")
        # 崩坏3签到
        return_data += checkin_game("honkai3rd", gamecheckin.Honkai3rd, "崩坏3rd")
        # 未定事件簿签到
        return_data += checkin_game("tears_of_themis", gamecheckin.TearsOfThemis, "未定事件簿")
        # 原神签到
        return_data += checkin_game("genshin", gamecheckin.Genshin, "原神")
        # 崩铁
        return_data += checkin_game("honkai_sr", gamecheckin.Honkaisr, "崩坏: 星穹铁道")
    # 国际
    if config.config['games']['os']["enable"]:
        log.info("海外版:")
        return_data += "\n\n" + "海外版:"
        if config.config['games']['os']['genshin']["auto_checkin"]:
            log.info("正在进行原神签到")
            data = hoyo_checkin.genshin()
            return_data += "\n\n" + data
        if config.config['games']['os']['honkai_sr']["auto_checkin"]:
            log.info("正在进行崩坏:星穹铁道签到")
            data = hoyo_checkin.honkai_sr()
            return_data += "\n\n" + data
    # 云游戏
    if config.config['cloud_games']['genshin']["enable"] \
            and config.config['cloud_games']['genshin']['token'] != "":
        log.info("正在进行云原神签到")
        cloud_ys = cloud_genshin.CloudGenshin()
        data = cloud_ys.sign_account()
        return_data += "\n\n" + data
    if "触发验证码" in return_data:
        ret_code = 3
    return ret_code, return_data


if __name__ == "__main__":
    try:
        status_code, message = main()
    except CookieError:
        status_code = 1
        message = "账号Cookie出错！"
        log.error("账号Cookie有问题！")
    push.push(status_code, message)
