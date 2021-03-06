#coding:utf-8


# -----------------------------doc--------------------------
# 工单 描述
WORKLIST_DOC = """
功能描述：生成一个H248开通工单

    参数：
    | MediaGatewayControler          | 172.24.242.251 | 处理H.248协议的软交换IP地址或者域名 |
    | Standby_MediaGatewayControler  | 172.24.242.251 | 备用处理H.248协议的软交换IP地址或者域名,如果为0,则不启用双归属 |
    | DeviceID                       | test | 终端向软交换平台注册时使用的全局唯一的标识 |
    | DeviceIDType                   | 1 | 终端标识的类型,如0:IP地址,1:域名,2:设备名 |
    | PhysicalTermID                 | 1 | 物理终结点标识，起始1 |
    | PhysicalTermIDPrefix           | A | 终端的物理终结点标识前缀 |
    | PhysicalTermIDAddLen           | 1 | 物理终结点标识的前缀后面添加的位数 |
    | PVC_OR_VLAN                    | PVC:0/63 | ADSL上行用PVC格式,LAN\GPON\VDSL则用VLAN格式,默认是ADSL的PVC |
    | X_CT_COM_ServiceList           | VOIP | WAN连接的服务模式,即X_CT-COM_ServiceList节点值,默认VOIP |
    | WANEnable_Switch               | True | WAN连接使能与WAN连接参数是否一起下发,True表示一起下发.默认为True |



    注意：此键字调用的是通配置的工单，如果想测逐个配置的工单（贝曼不支持，因为电信规范中没有相前节点配置），请执行另外的相应工单
"""


# -----------------------------args--------------------------
# 工单 参数
WORKLIST_ARGS = {
"MediaGatewayControler":("172.24.242.251","1"),
"Standby_MediaGatewayControler":("172.24.242.251","2"),
"DeviceID":("test","3"),
"DeviceIDType":("1","4"),
"PhysicalTermID":("1","5"),
"PhysicalTermIDPrefix":("A","6"),
"PhysicalTermIDAddLen":("1","7"),
# PVC or VLAN
"PVC_OR_VLAN":("PVC:0/63", "8"),
# 绑定的服务
"X_CT_COM_ServiceList":("VOIP", "9"),
# 最后的WAN连接使能动作是否单独下发
"WANEnable_Switch":("True", "10")
}
