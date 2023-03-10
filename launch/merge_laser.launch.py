
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    laser_relay_share = get_package_share_directory('laser_relay')

    laser_relay_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(laser_relay_share, 'launch',
                         'laser_relay.launch.py'),
        )
    )
    return LaunchDescription([
        DeclareLaunchArgument(name="topic_in1", default_value="/front_lidar_amr_mini_laser"),
        DeclareLaunchArgument(name="topic_in2", default_value="/back_lidar_amr_mini_laser"),
        DeclareLaunchArgument(name="topic_out", default_value="/scan"),
        laser_relay_launch
    ])
