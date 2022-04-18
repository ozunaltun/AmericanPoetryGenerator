# -*- coding: utf-8 -*-
"""Copy of Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mcomo8TYX5-S3E0oTJsN1oZkoJg7vKa0
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
!pip install gpt-2-simple
import gpt_2_simple as gpt2

gpt2.download_gpt2(model_name='124M')

file_name = "inputpoems.txt"

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset=file_name,
              model_name="124M",
              steps=200,
              restore_from="fresh",
              run_name="run1",
              print_every=10,
              sample_every=20,
              save_every=20)

gpt2.generate(sess,
              length=250,
              temperature=0.8,
              nsamples=5,
              batch_size=5,
              top_k=40
              )