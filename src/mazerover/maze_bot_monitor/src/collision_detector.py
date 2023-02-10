#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ContactsState

import csv
import os


class CollisionDetector(object):
    def __init__(self, name="/collision"):
        self.collision_sub = rospy.Subscriber(
            name, ContactsState, self.collision_callback, queue_size=10)
        self.event_log = []
        self.count = 0
        self.time_out = rospy.Time.now().to_sec()
        self.within_timeout = False
        self.backup_file = open(os.path.expanduser('~/.ros/backup_log'), 'w')
        self.backup_file_writer=csv.writer(self.backup_file)

    def collision_callback(self, msg):

        if len(msg.states) == 0:
            return

        cur_time = rospy.Time.now().to_sec()

        if cur_time > self.time_out:
            rospy.loginfo("Collsion Detected with Wall")
            self.count = self.count+1
            self.event_log.append(
                [self.count, cur_time, msg.states[0].collision1_name, msg.states[0].collision2_name])
            self.backup_file_writer.writerow(
                [self.count, cur_time, msg.states[0].collision1_name, msg.states[0].collision2_name])
            self.time_out = cur_time+float(10)

    def hook(self):
        try:
            with open(os.path.expanduser('~/.ros/team_id'), 'r') as file1:
                team_id = file1.readline()
                team_id = team_id.strip()
        except:
            team_id = 'log'

        try:
            # string = ''.join(random.choices(string.ascii_letters, k=10))
            # filename = team_id +'.csv'
            
            with open(os.path.expanduser('~/.ros/'+str(team_id)+'.csv'), 'w+') as f:
                writer = csv.writer(f)
                writer.writerows(self.event_log)
        except:
            with open(os.path.expanduser('~/.ros/log.csv'), 'w+') as f:
                writer = csv.writer(f)
                writer.writerows(self.event_log)
                
        self.backup_file.close()


if __name__ == "__main__":
    rospy.init_node("collision_detector")

    collision_detector = CollisionDetector()
    rospy.spin()
    rospy.on_shutdown(collision_detector.hook)
