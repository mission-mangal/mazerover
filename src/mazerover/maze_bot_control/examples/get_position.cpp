#include "control_utils.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "controller_node", ros::init_options::AnonymousName);
    ros::AsyncSpinner spinner(2);
    spinner.start();

    //############## Code starts here#################################

    // Creating the controller object
    Controller controller;

    // Checks if ros is ok
    while (ros::ok())
    {
        // Getting the location and printing
        auto position = controller.get_position();
        std::cout <<"x: " <<std::get<0>(position) << ",\ny: " << std::get<1>(position) << ",\ntheta(in radians): " << std::get<2>(position)<<"\n";

        // sleeping for 1 seconds
        ros::Duration(1).sleep();
    }

    //################## Code ends here####################################

    return 0;
}
