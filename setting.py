#米游社的Salt
mihoyobbs_Salt = "fd3ykrh7o1j54g581upo1tvpam0dsgtf"
mihoyobbs_Salt_web = "14bmu1mz0yuljprsfgpvjh3ju2ni468r"
mihoyobbs_Salt_web_old = "h8w582wxwgqvahcdkpvdhbh2w9casgfl"
#米游社的版本
mihoyobbs_Version = "2.7.0" #Slat和Version相互对应
mihoyobbs_Version_old = "2.3.0"
#米游社的客户端类型
mihoyobbs_Client_type = "2" #1为ios 2为安卓
mihoyobbs_Client_type_web = "5" #4为pc web 5为mobile web
#米游社的分区列表
mihoyobbs_List = [{
        "id": "1",
        "forumId": "1",
        "name": "崩坏3",
        "url": "https://bbs.mihoyo.com/bh3/"
    },{
        "id": "2",
        "forumId": "26",
        "name": "原神",
        "url": "https://bbs.mihoyo.com/ys/"
    },{
        "id": "3",
        "forumId": "30",
        "name": "崩坏2",
        "url": "https://bbs.mihoyo.com/bh2/"
    },{
        "id": "4",
        "forumId": "37",
        "name": "未定事件簿",
        "url": "https://bbs.mihoyo.com/wd/"
    },{
        "id": "5",
        "forumId": "34",
        "name": "大别野",
        "url": "https://bbs.mihoyo.com/dby/"
    }]

#Config Load之后run里面进行列表的选择
mihoyobbs_List_Use= []

#米游社的API列表
cookieUrl = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
cookieUrl2 = "https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
signUrl = "https://bbs-api.mihoyo.com/apihub/sapi/signIn?gids={}"  # post
listUrl = "https://bbs-api.mihoyo.com/post/api/getForumPostList?forum_id={}&is_good=false&is_hot=false&page_size=20&sort_type=1"
detailUrl = "https://bbs-api.mihoyo.com/post/api/getPostFull?post_id={}"
shareUrl = "https://bbs-api.mihoyo.com/apihub/api/getShareConf?entity_id={}&entity_type=1"
likeUrl = "https://bbs-api.mihoyo.com/apihub/sapi/upvotePost"  # post json 

#原神自动签到相关的设置
act_ID = "e202009291139501"
accinfo_Url = "https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn"