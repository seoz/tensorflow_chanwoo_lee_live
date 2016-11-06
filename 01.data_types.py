#Video link - https://www.youtube.com/watch?v=a74pFg8paVc&list=PL1H8jIvbSo1qlXVcdZTH2xsYFp3e1Nmjf&index=1

import tensorflow as tf

#placeholder, Variable, constant
ph = tf.placeholder(dtype=tf.float32, shape=[3,3])
var = tf.Variable([1, 2, 3, 4, 5], dtype=tf.float32)
const = tf.constant([10, 20, 30, 40, 50], dtype=tf.float32)

print ph
print var
print const

sess = tf.Session()
result = sess.run(const)
print result

#constant
a = tf.constant([5])
b = tf.constant([10])
c = tf.constant([2])
d = a * b + c
print d

sess = tf.Session()
result = sess.run(d)
print result

#Variable
var1 = tf.Variable([5])
var2 = tf.Variable([3])
var3 = tf.Variable([2])

var4 = var1 * var2 + var3
print var4

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)
result = sess.run(var4)
print result

#placeholder
value1 = 5
value2 = 3
value3 = 2

ph1 = tf.placeholder(dtype=tf.float32)
ph2 = tf.placeholder(dtype=tf.float32)
ph3 = tf.placeholder(dtype=tf.float32)

result_value = ph1 * ph2 + ph3

feed_dict = {ph1: value1, ph2: value2, ph3: value3}

sess = tf.Session()
result = sess.run(result_value, feed_dict=feed_dict)
print result