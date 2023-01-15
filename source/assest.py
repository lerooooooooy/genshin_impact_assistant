import text_manager
import img_manager
import button_manager
from util import *
# import scene_manager
QTSX = text_manager.TextTemplate(text=
{
    "zh_CN":"七天神像",
    "en_US":"Statues of The Seven"
}, cap_area = img_manager.bigmap_choose_area.cap_posi)
CSMD = text_manager.TextTemplate(text=
{
    "zh_CN":"传送锚点",
    "en_US": "Teleport Waypoint"
}, cap_area = img_manager.bigmap_choose_area.cap_posi)
LEAVINGIN = text_manager.TextTemplate(text=
{
    'zh_CN': '自动退出',
    "en_US": 'Leaving in'
}, cap_area = get_bbox(cv2.imread(os.path.join(root_path, "assests\\imgs\\common\\area\\LEAVINGIN.jpg"))))
claim_rewards = text_manager.TextTemplate(text=
{
    'zh_CN': '领取奖励',
    "en_US": "Claim Rewards"
})
use_20x2resin = text_manager.TextTemplate(text=
{
    'zh_CN': '使用浓缩树脂',
    "en_US": "Use Condensed Resin"
})
use_20resin = text_manager.TextTemplate(text=
{
    'zh_CN': '使用原粹树脂',
    "en_US": "Use Original Resin"
})
LEYLINEDISORDER = text_manager.TextTemplate(text=
{
    'zh_CN': '地脉异常',
    "en_US": "Ley Line Disorder"
}, cap_area = get_bbox(cv2.imread(os.path.join(root_path, "assests\\imgs\\common\\area\\LEYLINEDISORDER.jpg"))))
conti_challenge = text_manager.TextTemplate(text=
{
    'zh_CN': '继续挑战',
    "en_US": "Continue Challenge"
})
exit_challenge = text_manager.TextTemplate(text=
{
    'zh_CN': '退出秘境',
    "en_US": "Leave Domain"
})
domain_obtain = text_manager.TextTemplate(text=
{
    'zh_CN': '获得',
    "en_US": "Obtained"
})