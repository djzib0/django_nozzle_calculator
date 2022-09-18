let diameterInput = document.getElementById("diameter_input")
let profileInput = document.getElementById("profile_input")
let drawingInput = document.getElementById("drawing_input")
let profileHeightInput = document.getElementById("profile_height_input")
let InnerRingTypeInput = document.getElementById("inner_ring_type_input")
let InnerRingThicknessPropellerZoneInput = document.getElementById("inner_ring_thickness_propeller_zone_input")
let InnerRingThicknessInletZoneInput = document.getElementById("inner_ring_thicknes_inlet_zone_input")
let InnerRingThicknessOutletZoneInput = document.getElementById("inner_ring_thickness_outlet_zone_input")
let ribsThicknessInput = document.getElementById("ribs_thickness_input")
let ribsQuantityInput = document.getElementById("ribs_quantity_input")
let segmentsThicknessInput = document.getElementById("segments_thickness_input")
let segmentsQuantityInput = document.getElementById("segments_quantity_input")
let hasHeadboxInput = document.getElementById("has_headbox_input")
let hasOutletRingInput = document.getElementById("has_outlet_ring_input")

function resetForm() {
    diameterInput.innerText = ''
    profileInput.innerText = ''
    drawingInput.innerText = ''
    profileHeightInput.innerText = ''
    InnerRingTypeInput.innerText = ''
    InnerRingThicknessPropellerZoneInput.innerText = ''
    InnerRingThicknessInletZoneInput.innerText = ''
    InnerRingThicknessOutletZoneInput.innerText = ''
    ribsThicknessInput.innerText = ''
    ribsQuantityInput.innerText = ''
    segmentsThicknessInput.innerText = ''
    segmentsQuantityInput.innerText = ''
    hasHeadboxInput.innerText = ''
    hasOutletRingInput.innerText = ''
}
