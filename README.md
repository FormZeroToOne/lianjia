这个项目是爬取链家二手房的网站数据，用来分析二手房北京市场的份额
爬到的数据会发送到kafka中的topic里，然后使用flume 去采集数据，放到hdfs上，保存的文件格式是json，没有采用压缩，然后使用spark去分析数据，把分析好的数据
直接写到mysql中，最后使用springboot+mybatis+angular.js+echarts进行数据可视化.
用到的技术:

1.python+scrapy进行网站数据爬取<br>
2.kafka+flume数据采集<br>
3.hdfs 数据存储<br>
4.sparkcore + spark sql  数据分析<br>
5.springboot + mybatis + mysql + angular.js+echarts 完成数据可视化<br>
