# coding: utf-8

def getRegions():
    '''获取所有区域名字'''

    luohu = ["/ershoufang/buxin/", # 布心
             "/ershoufang/baishida/", # 百仕达
             "/ershoufang/cuizhu/", # 翠竹
             "/ershoufang/chunfenglu/", # 春风路
             "/ershoufang/dongmen/", # 东门
             "/ershoufang/diwang/", # 地王
             "/ershoufang/honghu/", # 洪湖
             "/ershoufang/huangbeiling/", # 黄贝岭
             "/ershoufang/luohukouan/", # 罗湖口岸
             "/ershoufang/liantang/", # 莲塘
             "/ershoufang/qingshuihe/", # 清水河
             "/ershoufang/sungang/", # 笋岗
             "/ershoufang/wanxiangcheng/", # 万象城
             "/ershoufang/xinxiu/", # 新秀
             "/ershoufang/yinhu/"] # 银湖

    futian = ["/ershoufang/baihua/", # 百花
              "/ershoufang/bijiashan/", # 笔架山
              "/ershoufang/bagualing/", # 八卦岭
              "/ershoufang/chegongmiao/", # 车公庙
              "/ershoufang/futianzhongxin/", # 福田中心
              "/ershoufang/futianbaoshuiqu/", # 福田保税区
              "/ershoufang/huaqiangnan/", # 华强南
              "/ershoufang/huaqiangbei/", # 华强北
              "/ershoufang/huanggang/", # 皇岗
              "/ershoufang/huaqiaocheng1/", # 华侨城
              "/ershoufang/jingtian/", # 景田
              "/ershoufang/lianhua/", # 莲花
              "/ershoufang/meilin/", # 梅林
              "/ershoufang/shangxiasha/", # 上下沙
              # "/ershoufang/shangbu/", # 上步  无房源
              "/ershoufang/shixia/", # 石厦
              "/ershoufang/xiangmihu/", # 香蜜湖
              "/ershoufang/xinzhou1/", # 新洲
              "/ershoufang/yuanling/", # 园岭
              "/ershoufang/zhuzilin/"] # 竹子林

    nanshan = ["/ershoufang/baishizhou/", # 白石洲
               "/ershoufang/daxuecheng3/", # 大学城
               "/ershoufang/houhai/", # 后海
               "/ershoufang/hongshuwan/", # 红树湾
               # "/ershoufang/huaqiaocheng1/", # 华侨城
               "/ershoufang/kejiyuan/", # 科技园
               "/ershoufang/nantou/", # 南头
               "/ershoufang/nanshanzhongxin/", # 南山中心
               "/ershoufang/qianhai/", # 前海
               "/ershoufang/shekou/", # 蛇口
               # "/ershoufang/shenzhenbeizhan/", # 深圳北站
               "/ershoufang/shenzhenwan/", # 深圳湾
               "/ershoufang/xili1/"] # 西丽

    yantian = ["/ershoufang/meisha/", # 梅沙
               "/ershoufang/shatoujiao/", # 沙头角
               "/ershoufang/yantiangang/"] # 盐田港

    baoan = ["/ershoufang/baoanzhongxin/", # 宝安中心
             "/ershoufang/fuyong/", # 福永
             "/ershoufang/gongming/", # 公明
             "/ershoufang/shajing/", # 沙井
             "/ershoufang/songgang/", # 松岗
             "/ershoufang/shiyan/", # 石岩
             "/ershoufang/taoyuanju/", # 桃源居
             "/ershoufang/xixiang/", # 西乡
             "/ershoufang/xicheng1/", # 曦城
             "/ershoufang/xinan/"] # 新安

    longgang = [# "/ershoufang/bantian/", # 坂田
                "/ershoufang/buji/", # 布吉
                "/ershoufang/henggang/", # 横岗
                "/ershoufang/longgangzhongxin/", # 龙岗中心
                "/ershoufang/nanlian/", # 南联
                "/ershoufang/pingdi/", # 坪地
                "/ershoufang/pingshan/", # 坪山
                "/ershoufang/pinghu/"] # 平湖

    longhua = ["/ershoufang/bantian/", # 坂田
               "/ershoufang/dalang/", # 大浪
               "/ershoufang/guanlan/", # 观澜
               "/ershoufang/longhuazhongxin/", # 龙华中心
               "/ershoufang/minzhi/", # 民治
               "/ershoufang/qinghu/", # 清湖
               "/ershoufang/shenzhenbeizhan/"] # 深圳北站


    region = {}
    region['luohu'] = luohu
    region['futian'] = futian
    region['nanshan'] = nanshan
    region['yantian'] = yantian
    region['baoan'] = baoan
    region['longgang'] = longgang
    region['longhua'] = longhua
    return region