
class Device:

    device_id = ""
 
    install_id = ""

    openudid=""

    imei = ""

    os_version=""

    cdid=""

    rom_version=""

    sdk_ver=""

    operator_name=""

    operator_id=""

    device_memory=""

    device_model=""

    xtttraceid=""

    mc=""

    ua =''

    device_brand =""

    def __init__(self, device_id="", install_id="", openudid="", imei="", os_version="", cdid="", rom_version="", sdk_ver="", operator_name="", operator_id="", device_memory="", device_model="", xtttraceid="", mc="", ua="", device_brand=""):
        self.device_id = device_id
        self.install_id = install_id
        self.openudid = openudid
        self.imei = imei
        self.os_version = os_version
        self.cdid = cdid
        self.rom_version = rom_version
        self.sdk_ver = sdk_ver
        self.operator_name = operator_name
        self.operator_id = operator_id
        self.device_memory = device_memory
        self.device_model = device_model
        self.xtttraceid = xtttraceid
        self.mc = mc
        self.ua = ua
        self.device_brand = device_brand