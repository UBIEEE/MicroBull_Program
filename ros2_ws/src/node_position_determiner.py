import rclpy
from std_msgs.msg import String

pub = rclpy.Publisher('topic_name', String, queue_size=10)
rclpy.init_node('node_name')
r = rclpy.Rate(10) 

while not rclpy.is_shutdown():
   pub.publish("hello world")
   r.sleep()