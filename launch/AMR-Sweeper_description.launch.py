
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro


def generate_launch_description():

    # The name of the package and path to xacro file within the package
    package_name = 'AMR-Sweeper_description'
    package_urdf = 'AMR-Sweeper.urdf.xacro'


    # Use xacro to process the file
    pkg_path = os.path.join(get_package_share_directory(package_name)
    xacro_file = os.path.join(pkg_path,'urdf',package_urdf)
    robot_description_raw = xacro.process_file(xacro_file).toxml()


    # Configure the state publisher node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw}]
    )


    # Run the nodes
    return LaunchDescription([
        node_robot_state_publisher
    ])
