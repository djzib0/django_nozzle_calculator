
import math

diameter = 3030
profile = 'Optima'
profile_height = 1515
inner_ring_type = 'Complete st. st. inside'
inner_ring_thickness_propeller_zone = 15
inner_ring_thickness_inlet_zone = 15
inner_ring_thickness_outlet_zone = 15
# if ring thickness in inlet/outlet zone is different than in propeller zone, calculate extra welding seam
ribs_quantity = 9
ribs_thickness = 20
segments_quantity = 3
segments_thickness = 16
has_headbox = True
has_outlet_ring = True

def calc_inner_ring_weld_mat_before_spinning(nozzle_height, ring_propeller_zone,
                                            ring_inlet_zone, ring_outlet_zone):
    """Calculates amount of welding wire for inner ring before spinning"""
    length = nozzle_height / 3000  # convert mm intro mtr
    inlet = round((calculate_butt_weld(length, ring_inlet_zone)), 1)
    outlet = round((calculate_butt_weld(length, ring_outlet_zone)), 1)
    propeller_zone = round((calculate_butt_weld(length, ring_propeller_zone)), 1)

    total = round((inlet + outlet + propeller_zone), 2)
    return total


def calc_inner_ring_welding_time_before_spinning(nozzle_height, ring_propeller_zone,
                                                 ring_inlet_zone, ring_outlet_zone):
    """Calculates amount of time required for welding inner ring before spinning"""

    welding_wire_amount = calc_inner_ring_weld_mat_before_spinning(nozzle_height, ring_propeller_zone, ring_inlet_zone,
                                                                   ring_outlet_zone)

    # print(welding_wire_amount * 0.7, "test")
    return round((welding_wire_amount * 0.7), 1)


def calc_welding_mat_segments_with_inner_ring(nozzle_diameter, segments_qty, segments_thick):
    """Calculates amount of welding wire required for welding segments with inner ring"""
    WELDING_MATERIAL_AMOUNT = {8: 0.12,
                               10: 0.2,
                               12: 0.31,
                               14: 0.46,
                               15: 0.51,
                               16: 0.55,
                               18: 0.65,
                               20: 0.65,
                               22: 0.81,
                               25: 0.99,
                               30: 1.2
                               }
    nozzle_diameter = nozzle_diameter / 1000
    result = nozzle_diameter * math.pi * segments_qty * 2 * WELDING_MATERIAL_AMOUNT[segments_thick]
    result = round(result, 1)
    print("Wynik: ", result)
    return result


def calc_welding_time_segments_with_inner_ring(nozzle_diameter, segments_qty, segments_thick):
    """Calculates amount of time required for welding inner ring before spinning"""

    welding_wire_amount = calc_welding_mat_segments_with_inner_ring(nozzle_diameter, segments_qty, segments_thick)

    # print(welding_wire_amount * 0.7, "test")
    print("Godziny: ", round((welding_wire_amount * 0.7), 1))
    return round((welding_wire_amount * 0.7), 1)




# Functions - mutli usage (i.e. the same way of calculating inner ring welding and outside cone plates
def calculate_butt_weld(length, plate_thickness):
    WELDING_MATERIAL_AMOUNT = {8: 0.79,
                               10: 1.19,
                               12: 1.67,
                               14: 2.23,
                               15: 2.54,
                               16: 2.87,
                               18: 3.59,
                               20: 4.59,
                               22: 5.27,
                               25: 6.55,
                               30: 8.87,
                               }

    result = WELDING_MATERIAL_AMOUNT[plate_thickness] * length * 1.15
    result = round(result, 1)
    return result


calc_inner_ring_welding_time_before_spinning(profile_height, inner_ring_thickness_propeller_zone,
                                                 inner_ring_thickness_inlet_zone, inner_ring_thickness_outlet_zone)


calc_welding_mat_segments_with_inner_ring(diameter, segments_quantity, segments_thickness)

calc_welding_time_segments_with_inner_ring(diameter, segments_quantity, segments_thickness)


