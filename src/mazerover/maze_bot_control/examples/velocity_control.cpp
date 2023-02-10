#include "control_utils.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "controller_node", ros::init_options::AnonymousName);
    ros::AsyncSpinner spinner(2);
    spinner.start();

    //############## Code starts here#################################

    // Creating the controller object
    Controller controller;

    int x, y, theta;

    // Checks if ros is ok
    while (true)
    {
        // if current x position is greater than 1.1, goes back and
        // if current x position is less than 0.9, goes front
        auto position = controller.get_position();
        std::tie(x, y, theta) = position;
        if (x > 1.1)
            controller.go_back();
        else if (x < 0.9)
            controller.go_front();
        else
            break;
    }

    //################## Code ends here####################################

    return 0;
}
