#include <ros/ros.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/Twist.h>
#include <tf/transform_datatypes.h>

class Controller
{
private:
    ros::NodeHandle nh_;
    ros::Subscriber sub_;
    ros::Publisher pub_;
    double x_, y_, theta_;

    double scale_;
    double speed_;
    double turn_;

public:
    Controller()
    {
        sub_ = nh_.subscribe("ground_truth", 1, &Controller::location_callback, this);
        pub_ = nh_.advertise<geometry_msgs::Twist>("cmd_vel", 1);
    }

    void location_callback(const nav_msgs::OdometryConstPtr &msg)
    {
        x_ = msg->pose.pose.position.x;
        y_ = msg->pose.pose.position.y;

        tf::Quaternion quat;
        tf::quaternionMsgToTF(msg->pose.pose.orientation, quat);
        tf::Matrix3x3 m(quat);
        double roll, pitch, yaw;
        m.getRPY(roll, pitch, yaw);
        theta_ = yaw;
    }

    /**
     * @brief Get the location rover with x,y coordinate and angle of rotation
     *
     * @return std::tuple <x_coordinate,y_coordinate, theta> <meter, meter, radian>
     */
    std::tuple<double, double, double> get_position()
    {
        return std::make_tuple(x_, y_, theta_);
    }

    /**
     * @brief Set the velocity scale object
     *
     * @param scale
     */
    void set_velocity_scale(double scale)
    {
        this->scale_ = scale;
    }

    void go_(int linear_direc, int angular_direc)
    {
        geometry_msgs::Twist twist;
        twist.linear.x = linear_direc * this->speed_ * this->scale_;
        twist.angular.z = angular_direc * this->turn_ * this->scale_;

        pub_.publish(twist);
    }

    void go_front()
    {
        this->go_(1, 0);
    }

    void go_back()
    {
        this->go_(-1, 0);
    }

    void rotate_left()
    {
        this->go_(0, 1);
    }

    void rotate_right()
    {
        this->go_(0, -1);
    }
};

// int main(int argc, char **argv)
// {
//     ros::init(argc, argv, "controller_node",ros::init_options::AnonymousName);

//     Controller controller;

//     ros::AsyncSpinner spinner(2);
//     spinner.start();

//     ros::Duration(5).sleep();
//     auto position=controller.get_position();
//     std::cout << std::get<0>(position) << "," << std::get<1>(position) << "," << std::get<2>(position);

//     return 0;
// }
