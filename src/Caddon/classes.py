from .operators.caddon_ot_origin_to_selected import CADDON_OT_OriginToSelected
from .panels.caddon_pt_main import CADDON_PT_Main
from .operators.caddon_ot_cursor_to_selected import CADDON_OT_CursorToSelected
from .operators.caddon_ot_snap_apply_all_transforms import CADDON_OT_SnapApplyAllTransforms
from .operators.caddon_ot_view import CADDON_OT_View

CLASSES = (
    CADDON_OT_OriginToSelected,
    CADDON_OT_CursorToSelected,
    CADDON_OT_SnapApplyAllTransforms,
    CADDON_PT_Main,
    CADDON_OT_View
)
