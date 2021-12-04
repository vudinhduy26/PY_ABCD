# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 00:12:49 2021

@author: duy
"""
import tensorflow as tf
a = tf.add(3,5,name="Addition")
with tf.compat.v1.Session() as sess:
    # Building a graph
    hello = tf.constant(a)
    writer = tf.keras.callbacks.TensorBoard(log_dir='logs_add', histogram_freq=0, write_graph=True,write_images=False, update_freq='epoch', profile_batch=2,embeddings_freq=0, embeddings_metadata=None)
print(sess.run(hello))