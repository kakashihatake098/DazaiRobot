import threading

from sqlalchemy import Column, String

from DazaiRobot.modules.sql import BASE, SESSION


class DazaiChats(BASE):
    __tablename__ = "dazai_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


DazaiChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_dazai(chat_id):
    try:
        chat = SESSION.query(DazaiChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_dazai(chat_id):
    with INSERTION_LOCK:
        dazaichat = SESSION.query(DazaiChats).get(str(chat_id))
        if not dazaichat:
            dazaichat = DazaiChats(str(chat_id))
        SESSION.add(dazaichat)
        SESSION.commit()


def rem_dazai(chat_id):
    with INSERTION_LOCK:
        dazaichat = SESSION.query(DazaiChats).get(str(chat_id))
        if dazaichat:
            SESSION.delete(dazaichat)
        SESSION.commit()
