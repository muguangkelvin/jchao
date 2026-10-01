import os
import json
import re

SITE_ROOT = r"c:\Users\USER\Desktop\博客\jchao.xyz"

# 28 Providers details
PROVIDERS = [
    {
        "rank": 1,
        "name": "灵动云",
        "slug": "lingdong-cloud",
        "url": "https://varnexa.lingdongaff.com/#/?code=JoIy7bO1",
        "price": "15元/月起",
        "traffic": "100GB - 1000GB/月",
        "nodes": "IPLC/IEPL专线，包含港台日新美韩等30+节点",
        "features": "4K超高清秒开、0丢包低延迟、解锁ChatGPT/Claude/Netflix/Disney+、全平台一键导入",
        "suitable": "追求极致稳定与超低延迟的硬核用户、跨境电商办公、4K/8K影音发烧友"
    },
    {
        "name": "暮光网络",
        "rank": 2,
        "slug": "twilight-network",
        "url": "https://varnexa.twilightaff.com/#/?code=KvGly3jY",
        "price": "20元/月起",
        "traffic": "120GB - 1500GB/月",
        "nodes": "晚高峰优化BGP/专线，40+全球优质出口",
        "features": "晚高峰流畅不卡顿、原生IP解锁流媒体、支持Shadowrocket/Clash/Sing-box",
        "suitable": "追剧看4K视频、外服游戏玩家、多设备同时在线用户"
    },
    {
        "name": "飞猫云",
        "rank": 3,
        "slug": "flycat-cloud",
        "url": "https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH",
        "price": "7元/月起 (84元/年)",
        "traffic": "50GB - 300GB/月",
        "nodes": "IEPL专线/直连轻量节点，香港/日本/新加坡优化",
        "features": "极致高性价比、自研小白客户端、小流量年付首选、新手开箱即用",
        "suitable": "预算有限的小白用户、备用梯子需求、轻度网页浏览与社交APP使用"
    },
    {
        "name": "微风网络",
        "rank": 4,
        "slug": "breezenet",
        "url": "https://edp01.breezenetaff.com/#/?code=He4n3zxg",
        "price": "11元/月起",
        "traffic": "100GB/月",
        "nodes": "多出口BGP高速节点、SS/Trojan高级协议",
        "features": "高抗封锁能力、节点更新稳定、支持多设备共享、无缝切换",
        "suitable": "日常办公、学习查资料、多平台连接用户"
    },
    {
        "name": "隐形人",
        "rank": 5,
        "slug": "invisible-man",
        "url": "https://varnexa.invisibleaff.com/#/?code=FlyoraeM",
        "price": "18元/月起",
        "traffic": "150GB/月",
        "nodes": "匿名安全代理专线，全球20+国家地区",
        "features": "主打网络隐私保护、零日志记录、高强度加密、防DNS污染",
        "suitable": "注重个人隐私安全、跨境支付、加密通信用户"
    },
    {
        "name": "浪网 WaveNet",
        "rank": 6,
        "slug": "wavenet",
        "url": "https://varnexa.wavenetaff.com/#/?code=a9HF4LBZ",
        "price": "22元/月起",
        "traffic": "200GB/月",
        "nodes": "海缆直连高速节点、亚太区低延迟专线",
        "features": "海量大带宽出口、游戏加速低丢包、支持Hysteria 2协议",
        "suitable": "Steam/Epic外服游戏加速、大文件下载、大流量用户"
    },
    {
        "name": "梯子云 LadderCloud",
        "rank": 7,
        "slug": "laddercloud",
        "url": "https://varnexa.ladderaff.com/#/?code=bYVSMHMh",
        "price": "16元/月起",
        "traffic": "120GB/月",
        "nodes": "多协议混合节点（Clash/v2rayN/Sing-box）",
        "features": "节点动态负载均衡、订阅自动更新、高可用防失联",
        "suitable": "小白新手、追求傻瓜式一键配置的用户"
    },
    {
        "name": "飞V",
        "rank": 8,
        "slug": "flyv",
        "url": "https://varnexa.flyvaff.com/#/?code=qaMgTyhY",
        "price": "19元/月起",
        "traffic": "160GB/月",
        "nodes": "VIP专属高速通道、美日港节点全覆盖",
        "features": "4K8K极速缓冲、独立高带宽节点、专享流媒体解锁",
        "suitable": "YouTube 4K画质高频观看者、TikTok跨境运营"
    },
    {
        "name": "星岛梦",
        "rank": 9,
        "slug": "xingdaomeng",
        "url": "https://kfccbb.xingdaomeng.com/#/?code=tLbhLnNf",
        "price": "15元/月起",
        "traffic": "100GB/月",
        "nodes": "新加坡/香港专线加速",
        "features": "针对东南亚及亚太节点深度优化、延迟表现稳定",
        "suitable": "亚太地区远程办公、跨境电商运营"
    },
    {
        "name": "光速云",
        "rank": 10,
        "slug": "guangsu-cloud",
        "url": "https://mdlky.gsyaff.com/#/?code=5snwJVcD",
        "price": "18元/月起",
        "traffic": "150GB/月",
        "nodes": "光纤直连中继专线",
        "features": "连接响应速度快、节点切换秒连、全平台客户端兼容",
        "suitable": "追求连接响应速度的用户"
    },
    {
        "name": "唯兔云",
        "rank": 11,
        "slug": "v2yun",
        "url": "https://fast.v2yunvipaff.com/#/?code=xkiG3YWN",
        "price": "12元/月起",
        "traffic": "100GB/月",
        "nodes": "V2Ray/Trojan全协议支持",
        "features": "经典老牌架构、多节点容灾重定向、稳定性高",
        "suitable": "追求老牌技术架构与高稳定度的用户"
    },
    {
        "name": "U1S1",
        "rank": 12,
        "slug": "u1s1",
        "url": "https://pkdj7.vipaff.cc/#/?code=nYbe5pKy",
        "price": "14元/月起",
        "traffic": "120GB/月",
        "nodes": "BGP多线接入",
        "features": "性价比出众、规则分流精准、不浪费流量",
        "suitable": "精细化流量分流需求者"
    },
    {
        "name": "极连云",
        "rank": 13,
        "slug": "jilian-cloud",
        "url": "https://kdjhao.jlyvipaff.com/#/?code=rO50GIZj",
        "price": "20元/月起",
        "traffic": "180GB/月",
        "nodes": "极速IPLC中转",
        "features": "极速穿越封锁、支持多设备并发、游戏延迟低",
        "suitable": "多设备并发使用与游戏加速需求"
    },
    {
        "name": "全球云",
        "rank": 14,
        "slug": "quanqiu-cloud",
        "url": "https://sswdh.gcvipaff.com/#/?code=Ys0xKqnU",
        "price": "20元/月起",
        "traffic": "120GB - 1500GB/月",
        "nodes": "全球50+国家地区机房",
        "features": "节点覆盖极其广泛、智能出口分流、支持多种订阅格式",
        "suitable": "需要多国IP切换、跨境业务测试"
    },
    {
        "name": "光年梯",
        "rank": 15,
        "slug": "guangnian-ti",
        "url": "https://ggmq.gntaff.com/#/?code=34i9Naos",
        "price": "16元/月起",
        "traffic": "130GB/月",
        "nodes": "光年专线节点",
        "features": "超长在线率保障、节点自动故障转移",
        "suitable": "长时间挂机、挂载后台服务用户"
    },
    {
        "name": "Sogo云",
        "rank": 16,
        "slug": "sogo-cloud",
        "url": "https://wzjc.sogoyunaff.cc/#/?code=nWA62UuJ",
        "price": "13元/月起",
        "traffic": "90GB/月",
        "nodes": "搜狗技术架构优化出口",
        "features": "节点简洁实用、无复杂门槛、导入即可用",
        "suitable": "零基础小白入门用户"
    },
    {
        "name": "宇宙云",
        "rank": 17,
        "slug": "yuzhou-cloud",
        "url": "https://wzjc.yuzoucloud.cc/#/?code=hMqs74rd",
        "price": "25元/月起",
        "traffic": "300GB/月",
        "nodes": "宇宙级超大带宽节点",
        "features": "超大流量套餐、适合团队共享或重度下载",
        "suitable": "工作室、团队共享、大文件下载"
    },
    {
        "name": "二猫云",
        "rank": 18,
        "slug": "ermao-cloud",
        "url": "https://waaa.2maoyunaff.cc/#/?code=tbIH9UGF",
        "price": "10元/月起",
        "traffic": "80GB/月",
        "nodes": "轻量优化线路",
        "features": "价格亲民、充值灵活、支持按量付费套餐",
        "suitable": "学生党、偶尔翻墙查询资料者"
    },
    {
        "name": "一翻云",
        "rank": 19,
        "slug": "yifan-cloud",
        "url": "https://wzjc.1flyunaff.cc/#/?code=vq9IugSn",
        "price": "15元/月起",
        "traffic": "110GB/月",
        "nodes": "一键翻墙优化专线",
        "features": "客户端一键更新配置、自动过滤失效节点",
        "suitable": "不喜欢复杂设置的操作小白"
    },
    {
        "name": "边缘节点 EdgeNova",
        "rank": 20,
        "slug": "edgenova",
        "url": "https://work.edgenovaaff.cc/#/?code=6Mi7km72",
        "price": "28元/月起",
        "traffic": "250GB/月",
        "nodes": "EdgeNova边缘加速网络",
        "features": "边缘计算加速节点、网页加载极其丝滑",
        "suitable": "追求网页瞬时加载体验的极客用户"
    },
    {
        "name": "可信云",
        "rank": 21,
        "slug": "kexin-cloud",
        "url": "https://work.kosingaff.com/#/?code=BmIpbeEn",
        "price": "17元/月起",
        "traffic": "120GB/月",
        "nodes": "高可信度企业中继",
        "features": "99.9%高可用 SLA、节点冗余备份",
        "suitable": "外贸沟通、企业跨境邮件"
    },
    {
        "name": "速界 SuJie",
        "rank": 22,
        "slug": "sujie",
        "url": "https://work.speedworldaff.cc/#/?code=YhcpJLbr",
        "price": "21元/月起",
        "traffic": "170GB/月",
        "nodes": "高速跨国中转专线",
        "features": "优化网速瓶颈、游戏与视频双重加速",
        "suitable": "全能型发烧友用户"
    },
    {
        "name": "快狸 KuaiLi",
        "rank": 23,
        "slug": "kuaili",
        "url": "https://work.kuailicloud.cc/#/?code=7BsufMC0",
        "price": "14元/月起",
        "traffic": "100GB/月",
        "nodes": "快狸极速通道",
        "features": "移动端体验优化、小火箭一键导入最顺畅",
        "suitable": "iOS小火箭（Shadowrocket）高频用户"
    },
    {
        "name": "无忧",
        "rank": 24,
        "slug": "worryfree",
        "url": "https://wep01.worryfreeaff.com/#/?code=vak0gPse",
        "price": "15元/月起",
        "traffic": "110GB/月",
        "nodes": "无忧防封锁节点",
        "features": "敏感时期依然稳定在线、自动切换最新协议",
        "suitable": "需要强力防封防失联梯子的用户"
    },
    {
        "name": "灵猫",
        "rank": 25,
        "slug": "civet",
        "url": "https://vip02.civetaff.com/#/?code=Z4KLo3Wz",
        "price": "16元/月起",
        "traffic": "130GB/月",
        "nodes": "灵猫智能分流线路",
        "features": "精准识别国内 traffic 避免损耗、省流省电",
        "suitable": "手机常驻后台翻墙用户"
    },
    {
        "name": "闪跃 FlashLeap",
        "rank": 26,
        "slug": "flashleap",
        "url": "https://vip02.flashleapaff.com/#/?code=wnLaKVaU",
        "price": "22元/月起",
        "traffic": "180GB/月",
        "nodes": "闪跃专线中继",
        "features": "毫秒级响应、流媒体秒开不缓冲",
        "suitable": "追求极致响应速度的科技爱好者"
    },
    {
        "name": "飞为 Firefly",
        "rank": 27,
        "slug": "firefly",
        "url": "https://vip02.fireflyaff.com/#/?code=1n1ZIJab",
        "price": "18元/月起",
        "traffic": "140GB/月",
        "nodes": "萤火虫全球代理网",
        "features": "界面清爽、无缝订阅更新、节点丰富",
        "suitable": "追求纯净体验的现代互联网用户"
    },
    {
        "name": "跨界",
        "rank": 28,
        "slug": "kuajie",
        "url": "https://vip02.kuajieaff.com/#/?code=RQ4b2tfV",
        "price": "20元/月起",
        "traffic": "160GB/月",
        "nodes": "跨界电商与游戏专线",
        "features": "多IP出口支持、ChatGPT及TikTok原生解锁",
        "suitable": "跨境电商自媒体、AI工具深度开发者"
    }
]

print(f"Loaded {len(PROVIDERS)} providers.")
