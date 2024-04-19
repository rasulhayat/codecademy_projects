class DriveBot:
    # Updated this constructor!
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!

# print(robot_2.motor_speed)
# print(robot_2.direction)
# print(robot_2.sensor_range)
# sensor_range defaults to 10
test_bot_1 = DriveBot(10, 270)

# direction defaults to 180
test_bot_2 = DriveBot(sensor_range=20, motor_speed=45)

# direction defaults to 180 and sensor_range defaults to 10
test_bot_3 = DriveBot(50)

# all default values are used
test_bot_4 = DriveBot()

# no default values are used
test_bot_5 = DriveBot(18, 95, 30)
