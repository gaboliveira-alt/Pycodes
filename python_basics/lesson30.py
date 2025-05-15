velocity = 61
car_local = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1


pass_car_velocity_radar_1 = velocity > RADAR_1
pass_car_radar_1 = car_local >= (LOCAL_1 - RADAR_RANGE) and \
    car_local <= (LOCAL_1 + RADAR_RANGE)
tax_car = pass_car_velocity_radar_1 and pass_car_radar_1


if pass_car_velocity_radar_1:
    print("A velocidade do carro passou no radar 1")

if pass_car_radar_1:
    print("O carro passou no radar 1")
    
if tax_car:
    print("O carro foi multado no radar 1")

