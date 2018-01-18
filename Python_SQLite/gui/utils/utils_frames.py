#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clear_frame(self, frame):
    """Destroy all the widget in a frame"""
    for widget in frame.winfo_children():   
        widget.destroy() 