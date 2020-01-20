#!/usr/bin/env bash


mkdir input_sr_yuv

mkdir input

mkdir output_sr_yuv

mkdir output

move input*.png input

move input*.yuv input_sr_yuv

move input*.p010 input_sr_yuv

move output*.png output

move output*.yuv output_sr_yuv

move output*.p010 output_sr_yuv



