from os import listdir, mkdir
from pyrogram import Client

from Bobby import config
from Bobby.calls.queues import clear, get, is_empty, put, task_done
from Bobby.calls import queues
from Bobby.calls.youtube import download
from Bobby.calls.calls import run, pytgcalls
from Bobby.calls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from Bobby.calls.convert import convert
