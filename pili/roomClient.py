import pili.api as api
import base64
import hmac
import hashlib


class RoomClient(object):
    """docstring for RoomClient"""
    def __init__(self, credentials):
        self.__credentials__ = credentials
        self.__auth__ = credentials.__auth__

    def createRoom(self, ownerId, roomName=None):
        res = api.create_room(self.__auth__, ownerId=ownerId, roomName=roomName)
        return res

    def getRoom(self, roomName):
        res = api.get_room(self.__auth__, roomName=roomName)
        return res

    def deleteRoom(self, roomName):
        res = api.delete_room(self.__auth__, roomName=roomName)
        return res

    def roomToken(self, roomName, userId, perm, expireAt):
        params = '{"room_name":"'+roomName+'","user_id":"'+userId+'","perm":"'+perm+'","expire_at":'+str(expireAt)+'}'
        roomAccessString = params
        encodedRoomAccess = base64.urlsafe_b64encode(roomAccessString)
        hashed = hmac.new(self.__auth__.secret_key, encodedRoomAccess, hashlib.sha1)
        encodedSign = base64.urlsafe_b64encode(hashed.digest())
        return self.__auth__.access_key+":"+encodedSign+":"+encodedRoomAccess
