import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import tf
from math import dist


class Controller:
    def __init__(self):
        self.current_location = None
        self.odometry_sub = rospy.Subscriber(
            'ground_truth', Odometry, self.location_callback)
        self.cmd_vel_pub_ = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.cmd_vel_pub1_ = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        self.speed_ = 0.4
        self.turn_ = 1.0
        self.scale_ = 1
        self.tolerence = 0.1
        self.rate_ = rospy.Rate(10)

    def location_callback(self, data):
        # Retrieve the current position (x, y)
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y

        # Retrieve the current orientation (theta)
        quaternion = (
            data.pose.pose.orientation.x,
            data.pose.pose.orientation.y,
            data.pose.pose.orientation.z,
            data.pose.pose.orientation.w
        )
        euler = tf.transformations.euler_from_quaternion(quaternion)
        theta = euler[2]

        # Update the current location
        self.current_location = (x, y, theta)

    def get_position(self):
        return self.current_location

    def set_velocity_scale(self, scale):
        self.scale_ = scale

    def go_(self, linear_direc, angular_direc):
        twist = Twist()
        twist.linear.x = linear_direc * self.speed_*self.scale_
        twist.angular.z = angular_direc * self.turn_*self.scale_

        self.cmd_vel_pub_.publish(twist)

    def go_front(self):
        self.go_(1, 0)

    def go_back(self):
        self.go_(-1, 0)

    def rotate_left(self):
        self.go_(0, 1)

    def rotate_right(self):
        self.go_(0, -1)

    def go_front(self, distance):
        steps = int(distance / 0.1)

        # Publish a constant velocity command for the required number of steps
        for _ in range(steps):
            cmd = Twist()
            cmd.linear.x = 0.1
            self.cmd_vel_pub1_.publish(cmd)
            self.rate_.sleep()

    def stop(self):
        # Publish a zero velocity command to stop the robot
        cmd = Twist()
        cmd.linear.x = 0.0
        self.cmd_vel_pub1_.publish(cmd)


if __name__ == '__main__':
    # Initialize the node
    rospy.init_node('controller_node', anonymous=True)
    controller = Controller()

    # Spin the node to keep it running
    rospy.spin()
