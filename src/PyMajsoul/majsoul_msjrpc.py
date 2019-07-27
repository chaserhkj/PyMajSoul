
from . import majsoul_pb2 as pb
from .msjrpc import MSJRpcService



class Lobby(MSJRpcService):
    _req = {
"fetchConnectionInfo": pb.ReqCommon,
"signup": pb.ReqSignupAccount,
"login": pb.ReqLogin,
"emailLogin": pb.ReqEmailLogin,
"oauth2Auth": pb.ReqOauth2Auth,
"oauth2Check": pb.ReqOauth2Check,
"oauth2Signup": pb.ReqOauth2Signup,
"oauth2Login": pb.ReqOauth2Login,
"createPhoneVerifyCode": pb.ReqCreatePhoneVerifyCode,
"createEmailVerifyCode": pb.ReqCreateEmailVerifyCode,
"verfifyCodeForSecure": pb.ReqVerifyCodeForSecure,
"bindPhoneNumber": pb.ReqBindPhoneNumber,
"bindEmail": pb.ReqBindEmail,
"modifyPassword": pb.ReqModifyPassword,
"bindAccount": pb.ReqBindAccount,
"logout": pb.ReqLogout,
"heatbeat": pb.ReqHeatBeat,
"createNickname": pb.ReqCreateNickname,
"modifyNickname": pb.ReqModifyNickname,
"modifyBirthday": pb.ReqModifyBirthday,
"fetchRoom": pb.ReqCommon,
"createRoom": pb.ReqCreateRoom,
"joinRoom": pb.ReqJoinRoom,
"leaveRoom": pb.ReqCommon,
"readyPlay": pb.ReqRoomReady,
"startRoom": pb.ReqRoomStart,
"kickPlayer": pb.ReqRoomKick,
"modifyRoom": pb.ReqModifyRoom,
"matchGame": pb.ReqJoinMatchQueue,
"cancelMatch": pb.ReqCancelMatchQueue,
"fetchAccountInfo": pb.ReqAccountInfo,
"changeAvatar": pb.ReqChangeAvatar,
"fetchAccountStatisticInfo": pb.ReqAccountStatisticInfo,
"fetchAccountCharacterInfo": pb.ReqCommon,
"shopPurchase": pb.ReqShopPurchase,
"fetchGameRecord": pb.ReqGameRecord,
"fetchGameRecordList": pb.ReqGameRecordList,
"fetchCollectedGameRecordList": pb.ReqCommon,
"fetchGameRecordsDetail": pb.ReqGameRecordsDetail,
"addCollectedGameRecord": pb.ReqAddCollectedGameRecord,
"removeCollectedGameRecord": pb.ReqRemoveCollectedGameRecord,
"changeCollectedGameRecordRemarks": pb.ReqChangeCollectedGameRecordRemarks,
"fetchLevelLeaderboard": pb.ReqLevelLeaderboard,
"fetchMultiAccountBrief": pb.ReqMultiAccountId,
"fetchFriendList": pb.ReqCommon,
"fetchFriendApplyList": pb.ReqCommon,
"applyFriend": pb.ReqApplyFriend,
"handleFriendApply": pb.ReqHandleFriendApply,
"removeFriend": pb.ReqRemoveFriend,
"searchAccountById": pb.ReqSearchAccountById,
"searchAccountByPattern": pb.ReqSearchAccountByPattern,
"fetchAccountState": pb.ReqAccountList,
"fetchBagInfo": pb.ReqCommon,
"useBagItem": pb.ReqUseBagItem,
"openManualItem": pb.ReqOpenManualItem,
"openRandomRewardItem": pb.ReqOpenRandomRewardItem,
"composeShard": pb.ReqComposeShard,
"fetchAnnouncement": pb.ReqCommon,
"readAnnouncement": pb.ReqReadAnnouncement,
"fetchMailInfo": pb.ReqCommon,
"readMail": pb.ReqReadMail,
"deleteMail": pb.ReqDeleteMail,
"takeAttachmentFromMail": pb.ReqTakeAttachment,
"fetchAchievement": pb.ReqCommon,
"buyShiLian": pb.ReqBuyShiLian,
"matchShiLian": pb.ReqCommon,
"goNextShiLian": pb.ReqCommon,
"updateClientValue": pb.ReqUpdateClientValue,
"fetchClientValue": pb.ReqCommon,
"clientMessage": pb.ReqClientMessage,
"fetchCurrentMatchInfo": pb.ReqCurrentMatchInfo,
"fetchReviveCoinInfo": pb.ReqCommon,
"gainReviveCoin": pb.ReqCommon,
"fetchDailyTask": pb.ReqCommon,
"refreshDailyTask": pb.ReqRefreshDailyTask,
"useGiftCode": pb.ReqUseGiftCode,
"fetchTitleList": pb.ReqCommon,
"useTitle": pb.ReqUseTitle,
"sendClientMessage": pb.ReqSendClientMessage,
"fetchGameLiveInfo": pb.ReqGameLiveInfo,
"fetchGameLiveLeftSegment": pb.ReqGameLiveLeftSegment,
"fetchGameLiveList": pb.ReqGameLiveList,
"fetchCommentSetting": pb.ReqCommon,
"updateCommentSetting": pb.ReqUpdateCommentSetting,
"fetchCommentList": pb.ReqFetchCommentList,
"fetchCommentContent": pb.ReqFetchCommentContent,
"leaveComment": pb.ReqLeaveComment,
"deleteComment": pb.ReqDeleteComment,
"updateReadComment": pb.ReqUpdateReadComment,
"fetchRollingNotice": pb.ReqCommon,
"fetchServerTime": pb.ReqCommon,
"fetchPlatformProducts": pb.ReqPlatformBillingProducts,
"createBillingOrder": pb.ReqCreateBillingOrder,
"solveGooglePlayOrder": pb.ReqSolveGooglePlayOrder,
"cancelGooglePlayOrder": pb.ReqCancelGooglePlayOrder,
"openChest": pb.ReqOpenChest,
"buyFromChestShop": pb.ReqBuyFromChestShop,
"fetchDailySignInInfo": pb.ReqCommon,
"doDailySignIn": pb.ReqCommon,
"fetchCharacterInfo": pb.ReqCommon,
"changeMainCharacter": pb.ReqChangeMainCharacter,
"changeCharacterSkin": pb.ReqChangeCharacterSkin,
"changeCharacterView": pb.ReqChangeCharacterView,
"sendGiftToCharacter": pb.ReqSendGiftToCharacter,
"sellItem": pb.ReqSellItem,
"fetchCommonView": pb.ReqCommon,
"changeCommonView": pb.ReqChangeCommonView,
"upgradeCharacter": pb.ReqUpgradeCharacter,
"gameMasterCommand": pb.ReqGMCommand,
"fetchShopInfo": pb.ReqCommon,
"buyFromShop": pb.ReqBuyFromShop,
"buyFromZHP": pb.ReqBuyFromZHP,
"refreshZHPShop": pb.ReqCommon,
"exchangeCurrency": pb.ReqExchangeCurrency,
"exchangeChestStone": pb.ReqExchangeCurrency,
"fetchServerSettings": pb.ReqCommon,
"fetchAccountSettings": pb.ReqCommon,
"updateAccountSettings": pb.ReqUpdateAccountSettings,
"fetchModNicknameTime": pb.ReqCommon,
"createWechatNativeOrder": pb.ReqCreateWechatNativeOrder,
"createWechatAppOrder": pb.ReqCreateWechatAppOrder,
"createAlipayOrder": pb.ReqCreateAlipayOrder,
"createAlipayScanOrder": pb.ReqCreateAlipayScanOrder,
"createAlipayAppOrder": pb.ReqCreateAlipayAppOrder,
"createJPCreditCardOrder": pb.ReqCreateJPCreditCardOrder,
"createJPPaypalOrder": pb.ReqCreateJPPaypalOrder,
"createJPAuOrder": pb.ReqCreateJPAuOrder,
"createJPDocomoOrder": pb.ReqCreateJPDocomoOrder,
"createJPSoftbankOrder": pb.ReqCreateJPSoftbankOrder,
"createENPaypalOrder": pb.ReqCreateENPaypalOrder,
"createENMasterCardOrder": pb.ReqCreateENMasterCardOrder,
"createENVisaOrder": pb.ReqCreateENVisaOrder,
"createENJCBOrder": pb.ReqCreateENJCBOrder,
"createENAlipayOrder": pb.ReqCreateENAlipayOrder,
"fetchMisc": pb.ReqCommon,
"modifySignature": pb.ReqModifySignature,
"fetchIDCardInfo": pb.ReqCommon,
"updateIDCardInfo": pb.ReqUpdateIDCardInfo,
"fetchVipReward": pb.ReqCommon,
"gainVipReward": pb.ReqGainVipReward,
"fetchCustomizedContestList": pb.ReqFetchCustomizedContestList,
"fetchCustomizedContestExtendInfo": pb.ReqFetchCustomizedContestExtendInfo,
"enterCustomizedContest": pb.ReqEnterCustomizedContest,
"leaveCustomizedContest": pb.ReqCommon,
"fetchCustomizedContestOnlineInfo": pb.ReqFetchCustomizedContestOnlineInfo,
"fetchCustomizedContestByContestId": pb.ReqFetchCustomizedContestByContestId,
"startCustomizedContest": pb.ReqStartCustomizedContest,
"stopCustomizedContest": pb.ReqCommon,
"joinCustomizedContestChatRoom": pb.ReqJoinCustomizedContestChatRoom,
"leaveCustomizedContestChatRoom": pb.ReqCommon,
"sayChatMessage": pb.ReqSayChatMessage,
"fetchCustomizedContestGameRecords": pb.ReqFetchCustomizedContestGameRecords,
"fetchCustomizedContestGameLiveList": pb.ReqFetchCustomizedContestGameLiveList,
"followCustomizedContest": pb.ReqTargetCustomizedContest,
"unfollowCustomizedContest": pb.ReqTargetCustomizedContest,
"fetchActivityList": pb.ReqCommon,
"fetchAccountActivityData": pb.ReqCommon,
"exchangeActivityItem": pb.ReqExchangeActivityItem,
"completeActivityTask": pb.ReqCompleteActivityTask,
"gainAccumulatedPointActivityReward": pb.ReqGainAccumulatedPointActivityReward,
"fetchRankPointLeaderboard": pb.ReqFetchRankPointLeaderboard,
"gainRankPointReward": pb.ReqGainRankPointReward,
    }
    _res = {
"fetchConnectionInfo": pb.ResConnectionInfo,
"signup": pb.ResSignupAccount,
"login": pb.ResLogin,
"emailLogin": pb.ResLogin,
"oauth2Auth": pb.ResOauth2Auth,
"oauth2Check": pb.ResOauth2Check,
"oauth2Signup": pb.ResOauth2Signup,
"oauth2Login": pb.ResLogin,
"createPhoneVerifyCode": pb.ResCommon,
"createEmailVerifyCode": pb.ResCommon,
"verfifyCodeForSecure": pb.ResVerfiyCodeForSecure,
"bindPhoneNumber": pb.ResCommon,
"bindEmail": pb.ResCommon,
"modifyPassword": pb.ResCommon,
"bindAccount": pb.ResCommon,
"logout": pb.ResLogout,
"heatbeat": pb.ResCommon,
"createNickname": pb.ResCommon,
"modifyNickname": pb.ResCommon,
"modifyBirthday": pb.ResCommon,
"fetchRoom": pb.ResSelfRoom,
"createRoom": pb.ResCreateRoom,
"joinRoom": pb.ResJoinRoom,
"leaveRoom": pb.ResCommon,
"readyPlay": pb.ResCommon,
"startRoom": pb.ResCommon,
"kickPlayer": pb.ResCommon,
"modifyRoom": pb.ResCommon,
"matchGame": pb.ResCommon,
"cancelMatch": pb.ResCommon,
"fetchAccountInfo": pb.ResAccountInfo,
"changeAvatar": pb.ResCommon,
"fetchAccountStatisticInfo": pb.ResAccountStatisticInfo,
"fetchAccountCharacterInfo": pb.ResAccountCharacterInfo,
"shopPurchase": pb.ResShopPurchase,
"fetchGameRecord": pb.ResGameRecord,
"fetchGameRecordList": pb.ResGameRecordList,
"fetchCollectedGameRecordList": pb.ResCollectedGameRecordList,
"fetchGameRecordsDetail": pb.ResGameRecordsDetail,
"addCollectedGameRecord": pb.ResAddCollectedGameRecord,
"removeCollectedGameRecord": pb.ResRemoveCollectedGameRecord,
"changeCollectedGameRecordRemarks": pb.ResChangeCollectedGameRecordRemarks,
"fetchLevelLeaderboard": pb.ResLevelLeaderboard,
"fetchMultiAccountBrief": pb.ResMultiAccountBrief,
"fetchFriendList": pb.ResFriendList,
"fetchFriendApplyList": pb.ResFriendApplyList,
"applyFriend": pb.ResCommon,
"handleFriendApply": pb.ResCommon,
"removeFriend": pb.ResCommon,
"searchAccountById": pb.ResSearchAccountById,
"searchAccountByPattern": pb.ResSearchAccountByPattern,
"fetchAccountState": pb.ResAccountStates,
"fetchBagInfo": pb.ResBagInfo,
"useBagItem": pb.ResCommon,
"openManualItem": pb.ResCommon,
"openRandomRewardItem": pb.ResOpenRandomRewardItem,
"composeShard": pb.ResCommon,
"fetchAnnouncement": pb.ResAnnouncement,
"readAnnouncement": pb.ResCommon,
"fetchMailInfo": pb.ResMailInfo,
"readMail": pb.ResCommon,
"deleteMail": pb.ResCommon,
"takeAttachmentFromMail": pb.ResCommon,
"fetchAchievement": pb.ResAchievement,
"buyShiLian": pb.ResCommon,
"matchShiLian": pb.ResCommon,
"goNextShiLian": pb.ResCommon,
"updateClientValue": pb.ResCommon,
"fetchClientValue": pb.ResClientValue,
"clientMessage": pb.ResCommon,
"fetchCurrentMatchInfo": pb.ResCurrentMatchInfo,
"fetchReviveCoinInfo": pb.ResReviveCoinInfo,
"gainReviveCoin": pb.ResCommon,
"fetchDailyTask": pb.ResDailyTask,
"refreshDailyTask": pb.ResRefreshDailyTask,
"useGiftCode": pb.ResUseGiftCode,
"fetchTitleList": pb.ResTitleList,
"useTitle": pb.ResCommon,
"sendClientMessage": pb.ResCommon,
"fetchGameLiveInfo": pb.ResGameLiveInfo,
"fetchGameLiveLeftSegment": pb.ResGameLiveLeftSegment,
"fetchGameLiveList": pb.ResGameLiveList,
"fetchCommentSetting": pb.ResCommentSetting,
"updateCommentSetting": pb.ResCommon,
"fetchCommentList": pb.ResFetchCommentList,
"fetchCommentContent": pb.ResFetchCommentContent,
"leaveComment": pb.ResCommon,
"deleteComment": pb.ResCommon,
"updateReadComment": pb.ResCommon,
"fetchRollingNotice": pb.ReqRollingNotice,
"fetchServerTime": pb.ResServerTime,
"fetchPlatformProducts": pb.ResPlatformBillingProducts,
"createBillingOrder": pb.ResCreateBillingOrder,
"solveGooglePlayOrder": pb.ResCommon,
"cancelGooglePlayOrder": pb.ResCommon,
"openChest": pb.ResOpenChest,
"buyFromChestShop": pb.ResBuyFromChestShop,
"fetchDailySignInInfo": pb.ResDailySignInInfo,
"doDailySignIn": pb.ResCommon,
"fetchCharacterInfo": pb.ResCharacterInfo,
"changeMainCharacter": pb.ResCommon,
"changeCharacterSkin": pb.ResCommon,
"changeCharacterView": pb.ResCommon,
"sendGiftToCharacter": pb.ResSendGiftToCharacter,
"sellItem": pb.ResCommon,
"fetchCommonView": pb.ResCommonView,
"changeCommonView": pb.ResCommon,
"upgradeCharacter": pb.ResUpgradeCharacter,
"gameMasterCommand": pb.ResCommon,
"fetchShopInfo": pb.ResShopInfo,
"buyFromShop": pb.ResBuyFromShop,
"buyFromZHP": pb.ResCommon,
"refreshZHPShop": pb.ResRefreshZHPShop,
"exchangeCurrency": pb.ResCommon,
"exchangeChestStone": pb.ResCommon,
"fetchServerSettings": pb.ResServerSettings,
"fetchAccountSettings": pb.ResAccountSettings,
"updateAccountSettings": pb.ResCommon,
"fetchModNicknameTime": pb.ResModNicknameTime,
"createWechatNativeOrder": pb.ResCreateWechatNativeOrder,
"createWechatAppOrder": pb.ResCreateWechatAppOrder,
"createAlipayOrder": pb.ResCreateAlipayOrder,
"createAlipayScanOrder": pb.ResCreateAlipayScanOrder,
"createAlipayAppOrder": pb.ResCreateAlipayAppOrder,
"createJPCreditCardOrder": pb.ResCreateJPCreditCardOrder,
"createJPPaypalOrder": pb.ResCreateJPPaypalOrder,
"createJPAuOrder": pb.ResCreateJPAuOrder,
"createJPDocomoOrder": pb.ResCreateJPDocomoOrder,
"createJPSoftbankOrder": pb.ResCreateJPSoftbankOrder,
"createENPaypalOrder": pb.ResCreateENPaypalOrder,
"createENMasterCardOrder": pb.ResCreateENMasterCardOrder,
"createENVisaOrder": pb.ResCreateENVisaOrder,
"createENJCBOrder": pb.ResCreateENJCBOrder,
"createENAlipayOrder": pb.ResCreateENAlipayOrder,
"fetchMisc": pb.ResMisc,
"modifySignature": pb.ResCommon,
"fetchIDCardInfo": pb.ResIDCardInfo,
"updateIDCardInfo": pb.ResCommon,
"fetchVipReward": pb.ResVipReward,
"gainVipReward": pb.ResCommon,
"fetchCustomizedContestList": pb.ResFetchCustomizedContestList,
"fetchCustomizedContestExtendInfo": pb.ResFetchCustomizedContestExtendInfo,
"enterCustomizedContest": pb.ResEnterCustomizedContest,
"leaveCustomizedContest": pb.ResCommon,
"fetchCustomizedContestOnlineInfo": pb.ResFetchCustomizedContestOnlineInfo,
"fetchCustomizedContestByContestId": pb.ResFetchCustomizedContestByContestId,
"startCustomizedContest": pb.ResCommon,
"stopCustomizedContest": pb.ResCommon,
"joinCustomizedContestChatRoom": pb.ResJoinCustomizedContestChatRoom,
"leaveCustomizedContestChatRoom": pb.ResCommon,
"sayChatMessage": pb.ResCommon,
"fetchCustomizedContestGameRecords": pb.ResFetchCustomizedContestGameRecords,
"fetchCustomizedContestGameLiveList": pb.ResFetchCustomizedContestGameLiveList,
"followCustomizedContest": pb.ResCommon,
"unfollowCustomizedContest": pb.ResCommon,
"fetchActivityList": pb.ResActivityList,
"fetchAccountActivityData": pb.ResAccountActivityData,
"exchangeActivityItem": pb.ResExchangeActivityItem,
"completeActivityTask": pb.ResCommon,
"gainAccumulatedPointActivityReward": pb.ResCommon,
"fetchRankPointLeaderboard": pb.ResFetchRankPointLeaderboard,
"gainRankPointReward": pb.ResCommon,
    }

    def get_package_name(self):
        return "lq"

    def get_service_name(self):
        return "Lobby"

    def get_req_class(self, method):
        return Lobby._req[method]

    def get_res_class(self, method):
        return Lobby._res[method]


    async def fetchConnectionInfo(self, req):
        return await self.call_method("fetchConnectionInfo", req)


    async def signup(self, req):
        return await self.call_method("signup", req)


    async def login(self, req):
        return await self.call_method("login", req)


    async def emailLogin(self, req):
        return await self.call_method("emailLogin", req)


    async def oauth2Auth(self, req):
        return await self.call_method("oauth2Auth", req)


    async def oauth2Check(self, req):
        return await self.call_method("oauth2Check", req)


    async def oauth2Signup(self, req):
        return await self.call_method("oauth2Signup", req)


    async def oauth2Login(self, req):
        return await self.call_method("oauth2Login", req)


    async def createPhoneVerifyCode(self, req):
        return await self.call_method("createPhoneVerifyCode", req)


    async def createEmailVerifyCode(self, req):
        return await self.call_method("createEmailVerifyCode", req)


    async def verfifyCodeForSecure(self, req):
        return await self.call_method("verfifyCodeForSecure", req)


    async def bindPhoneNumber(self, req):
        return await self.call_method("bindPhoneNumber", req)


    async def bindEmail(self, req):
        return await self.call_method("bindEmail", req)


    async def modifyPassword(self, req):
        return await self.call_method("modifyPassword", req)


    async def bindAccount(self, req):
        return await self.call_method("bindAccount", req)


    async def logout(self, req):
        return await self.call_method("logout", req)


    async def heatbeat(self, req):
        return await self.call_method("heatbeat", req)


    async def createNickname(self, req):
        return await self.call_method("createNickname", req)


    async def modifyNickname(self, req):
        return await self.call_method("modifyNickname", req)


    async def modifyBirthday(self, req):
        return await self.call_method("modifyBirthday", req)


    async def fetchRoom(self, req):
        return await self.call_method("fetchRoom", req)


    async def createRoom(self, req):
        return await self.call_method("createRoom", req)


    async def joinRoom(self, req):
        return await self.call_method("joinRoom", req)


    async def leaveRoom(self, req):
        return await self.call_method("leaveRoom", req)


    async def readyPlay(self, req):
        return await self.call_method("readyPlay", req)


    async def startRoom(self, req):
        return await self.call_method("startRoom", req)


    async def kickPlayer(self, req):
        return await self.call_method("kickPlayer", req)


    async def modifyRoom(self, req):
        return await self.call_method("modifyRoom", req)


    async def matchGame(self, req):
        return await self.call_method("matchGame", req)


    async def cancelMatch(self, req):
        return await self.call_method("cancelMatch", req)


    async def fetchAccountInfo(self, req):
        return await self.call_method("fetchAccountInfo", req)


    async def changeAvatar(self, req):
        return await self.call_method("changeAvatar", req)


    async def fetchAccountStatisticInfo(self, req):
        return await self.call_method("fetchAccountStatisticInfo", req)


    async def fetchAccountCharacterInfo(self, req):
        return await self.call_method("fetchAccountCharacterInfo", req)


    async def shopPurchase(self, req):
        return await self.call_method("shopPurchase", req)


    async def fetchGameRecord(self, req):
        return await self.call_method("fetchGameRecord", req)


    async def fetchGameRecordList(self, req):
        return await self.call_method("fetchGameRecordList", req)


    async def fetchCollectedGameRecordList(self, req):
        return await self.call_method("fetchCollectedGameRecordList", req)


    async def fetchGameRecordsDetail(self, req):
        return await self.call_method("fetchGameRecordsDetail", req)


    async def addCollectedGameRecord(self, req):
        return await self.call_method("addCollectedGameRecord", req)


    async def removeCollectedGameRecord(self, req):
        return await self.call_method("removeCollectedGameRecord", req)


    async def changeCollectedGameRecordRemarks(self, req):
        return await self.call_method("changeCollectedGameRecordRemarks", req)


    async def fetchLevelLeaderboard(self, req):
        return await self.call_method("fetchLevelLeaderboard", req)


    async def fetchMultiAccountBrief(self, req):
        return await self.call_method("fetchMultiAccountBrief", req)


    async def fetchFriendList(self, req):
        return await self.call_method("fetchFriendList", req)


    async def fetchFriendApplyList(self, req):
        return await self.call_method("fetchFriendApplyList", req)


    async def applyFriend(self, req):
        return await self.call_method("applyFriend", req)


    async def handleFriendApply(self, req):
        return await self.call_method("handleFriendApply", req)


    async def removeFriend(self, req):
        return await self.call_method("removeFriend", req)


    async def searchAccountById(self, req):
        return await self.call_method("searchAccountById", req)


    async def searchAccountByPattern(self, req):
        return await self.call_method("searchAccountByPattern", req)


    async def fetchAccountState(self, req):
        return await self.call_method("fetchAccountState", req)


    async def fetchBagInfo(self, req):
        return await self.call_method("fetchBagInfo", req)


    async def useBagItem(self, req):
        return await self.call_method("useBagItem", req)


    async def openManualItem(self, req):
        return await self.call_method("openManualItem", req)


    async def openRandomRewardItem(self, req):
        return await self.call_method("openRandomRewardItem", req)


    async def composeShard(self, req):
        return await self.call_method("composeShard", req)


    async def fetchAnnouncement(self, req):
        return await self.call_method("fetchAnnouncement", req)


    async def readAnnouncement(self, req):
        return await self.call_method("readAnnouncement", req)


    async def fetchMailInfo(self, req):
        return await self.call_method("fetchMailInfo", req)


    async def readMail(self, req):
        return await self.call_method("readMail", req)


    async def deleteMail(self, req):
        return await self.call_method("deleteMail", req)


    async def takeAttachmentFromMail(self, req):
        return await self.call_method("takeAttachmentFromMail", req)


    async def fetchAchievement(self, req):
        return await self.call_method("fetchAchievement", req)


    async def buyShiLian(self, req):
        return await self.call_method("buyShiLian", req)


    async def matchShiLian(self, req):
        return await self.call_method("matchShiLian", req)


    async def goNextShiLian(self, req):
        return await self.call_method("goNextShiLian", req)


    async def updateClientValue(self, req):
        return await self.call_method("updateClientValue", req)


    async def fetchClientValue(self, req):
        return await self.call_method("fetchClientValue", req)


    async def clientMessage(self, req):
        return await self.call_method("clientMessage", req)


    async def fetchCurrentMatchInfo(self, req):
        return await self.call_method("fetchCurrentMatchInfo", req)


    async def fetchReviveCoinInfo(self, req):
        return await self.call_method("fetchReviveCoinInfo", req)


    async def gainReviveCoin(self, req):
        return await self.call_method("gainReviveCoin", req)


    async def fetchDailyTask(self, req):
        return await self.call_method("fetchDailyTask", req)


    async def refreshDailyTask(self, req):
        return await self.call_method("refreshDailyTask", req)


    async def useGiftCode(self, req):
        return await self.call_method("useGiftCode", req)


    async def fetchTitleList(self, req):
        return await self.call_method("fetchTitleList", req)


    async def useTitle(self, req):
        return await self.call_method("useTitle", req)


    async def sendClientMessage(self, req):
        return await self.call_method("sendClientMessage", req)


    async def fetchGameLiveInfo(self, req):
        return await self.call_method("fetchGameLiveInfo", req)


    async def fetchGameLiveLeftSegment(self, req):
        return await self.call_method("fetchGameLiveLeftSegment", req)


    async def fetchGameLiveList(self, req):
        return await self.call_method("fetchGameLiveList", req)


    async def fetchCommentSetting(self, req):
        return await self.call_method("fetchCommentSetting", req)


    async def updateCommentSetting(self, req):
        return await self.call_method("updateCommentSetting", req)


    async def fetchCommentList(self, req):
        return await self.call_method("fetchCommentList", req)


    async def fetchCommentContent(self, req):
        return await self.call_method("fetchCommentContent", req)


    async def leaveComment(self, req):
        return await self.call_method("leaveComment", req)


    async def deleteComment(self, req):
        return await self.call_method("deleteComment", req)


    async def updateReadComment(self, req):
        return await self.call_method("updateReadComment", req)


    async def fetchRollingNotice(self, req):
        return await self.call_method("fetchRollingNotice", req)


    async def fetchServerTime(self, req):
        return await self.call_method("fetchServerTime", req)


    async def fetchPlatformProducts(self, req):
        return await self.call_method("fetchPlatformProducts", req)


    async def createBillingOrder(self, req):
        return await self.call_method("createBillingOrder", req)


    async def solveGooglePlayOrder(self, req):
        return await self.call_method("solveGooglePlayOrder", req)


    async def cancelGooglePlayOrder(self, req):
        return await self.call_method("cancelGooglePlayOrder", req)


    async def openChest(self, req):
        return await self.call_method("openChest", req)


    async def buyFromChestShop(self, req):
        return await self.call_method("buyFromChestShop", req)


    async def fetchDailySignInInfo(self, req):
        return await self.call_method("fetchDailySignInInfo", req)


    async def doDailySignIn(self, req):
        return await self.call_method("doDailySignIn", req)


    async def fetchCharacterInfo(self, req):
        return await self.call_method("fetchCharacterInfo", req)


    async def changeMainCharacter(self, req):
        return await self.call_method("changeMainCharacter", req)


    async def changeCharacterSkin(self, req):
        return await self.call_method("changeCharacterSkin", req)


    async def changeCharacterView(self, req):
        return await self.call_method("changeCharacterView", req)


    async def sendGiftToCharacter(self, req):
        return await self.call_method("sendGiftToCharacter", req)


    async def sellItem(self, req):
        return await self.call_method("sellItem", req)


    async def fetchCommonView(self, req):
        return await self.call_method("fetchCommonView", req)


    async def changeCommonView(self, req):
        return await self.call_method("changeCommonView", req)


    async def upgradeCharacter(self, req):
        return await self.call_method("upgradeCharacter", req)


    async def gameMasterCommand(self, req):
        return await self.call_method("gameMasterCommand", req)


    async def fetchShopInfo(self, req):
        return await self.call_method("fetchShopInfo", req)


    async def buyFromShop(self, req):
        return await self.call_method("buyFromShop", req)


    async def buyFromZHP(self, req):
        return await self.call_method("buyFromZHP", req)


    async def refreshZHPShop(self, req):
        return await self.call_method("refreshZHPShop", req)


    async def exchangeCurrency(self, req):
        return await self.call_method("exchangeCurrency", req)


    async def exchangeChestStone(self, req):
        return await self.call_method("exchangeChestStone", req)


    async def fetchServerSettings(self, req):
        return await self.call_method("fetchServerSettings", req)


    async def fetchAccountSettings(self, req):
        return await self.call_method("fetchAccountSettings", req)


    async def updateAccountSettings(self, req):
        return await self.call_method("updateAccountSettings", req)


    async def fetchModNicknameTime(self, req):
        return await self.call_method("fetchModNicknameTime", req)


    async def createWechatNativeOrder(self, req):
        return await self.call_method("createWechatNativeOrder", req)


    async def createWechatAppOrder(self, req):
        return await self.call_method("createWechatAppOrder", req)


    async def createAlipayOrder(self, req):
        return await self.call_method("createAlipayOrder", req)


    async def createAlipayScanOrder(self, req):
        return await self.call_method("createAlipayScanOrder", req)


    async def createAlipayAppOrder(self, req):
        return await self.call_method("createAlipayAppOrder", req)


    async def createJPCreditCardOrder(self, req):
        return await self.call_method("createJPCreditCardOrder", req)


    async def createJPPaypalOrder(self, req):
        return await self.call_method("createJPPaypalOrder", req)


    async def createJPAuOrder(self, req):
        return await self.call_method("createJPAuOrder", req)


    async def createJPDocomoOrder(self, req):
        return await self.call_method("createJPDocomoOrder", req)


    async def createJPSoftbankOrder(self, req):
        return await self.call_method("createJPSoftbankOrder", req)


    async def createENPaypalOrder(self, req):
        return await self.call_method("createENPaypalOrder", req)


    async def createENMasterCardOrder(self, req):
        return await self.call_method("createENMasterCardOrder", req)


    async def createENVisaOrder(self, req):
        return await self.call_method("createENVisaOrder", req)


    async def createENJCBOrder(self, req):
        return await self.call_method("createENJCBOrder", req)


    async def createENAlipayOrder(self, req):
        return await self.call_method("createENAlipayOrder", req)


    async def fetchMisc(self, req):
        return await self.call_method("fetchMisc", req)


    async def modifySignature(self, req):
        return await self.call_method("modifySignature", req)


    async def fetchIDCardInfo(self, req):
        return await self.call_method("fetchIDCardInfo", req)


    async def updateIDCardInfo(self, req):
        return await self.call_method("updateIDCardInfo", req)


    async def fetchVipReward(self, req):
        return await self.call_method("fetchVipReward", req)


    async def gainVipReward(self, req):
        return await self.call_method("gainVipReward", req)


    async def fetchCustomizedContestList(self, req):
        return await self.call_method("fetchCustomizedContestList", req)


    async def fetchCustomizedContestExtendInfo(self, req):
        return await self.call_method("fetchCustomizedContestExtendInfo", req)


    async def enterCustomizedContest(self, req):
        return await self.call_method("enterCustomizedContest", req)


    async def leaveCustomizedContest(self, req):
        return await self.call_method("leaveCustomizedContest", req)


    async def fetchCustomizedContestOnlineInfo(self, req):
        return await self.call_method("fetchCustomizedContestOnlineInfo", req)


    async def fetchCustomizedContestByContestId(self, req):
        return await self.call_method("fetchCustomizedContestByContestId", req)


    async def startCustomizedContest(self, req):
        return await self.call_method("startCustomizedContest", req)


    async def stopCustomizedContest(self, req):
        return await self.call_method("stopCustomizedContest", req)


    async def joinCustomizedContestChatRoom(self, req):
        return await self.call_method("joinCustomizedContestChatRoom", req)


    async def leaveCustomizedContestChatRoom(self, req):
        return await self.call_method("leaveCustomizedContestChatRoom", req)


    async def sayChatMessage(self, req):
        return await self.call_method("sayChatMessage", req)


    async def fetchCustomizedContestGameRecords(self, req):
        return await self.call_method("fetchCustomizedContestGameRecords", req)


    async def fetchCustomizedContestGameLiveList(self, req):
        return await self.call_method("fetchCustomizedContestGameLiveList", req)


    async def followCustomizedContest(self, req):
        return await self.call_method("followCustomizedContest", req)


    async def unfollowCustomizedContest(self, req):
        return await self.call_method("unfollowCustomizedContest", req)


    async def fetchActivityList(self, req):
        return await self.call_method("fetchActivityList", req)


    async def fetchAccountActivityData(self, req):
        return await self.call_method("fetchAccountActivityData", req)


    async def exchangeActivityItem(self, req):
        return await self.call_method("exchangeActivityItem", req)


    async def completeActivityTask(self, req):
        return await self.call_method("completeActivityTask", req)


    async def gainAccumulatedPointActivityReward(self, req):
        return await self.call_method("gainAccumulatedPointActivityReward", req)


    async def fetchRankPointLeaderboard(self, req):
        return await self.call_method("fetchRankPointLeaderboard", req)


    async def gainRankPointReward(self, req):
        return await self.call_method("gainRankPointReward", req)




class FastTest(MSJRpcService):
    _req = {
"authGame": pb.ReqAuthGame,
"enterGame": pb.ReqCommon,
"syncGame": pb.ReqSyncGame,
"finishSyncGame": pb.ReqCommon,
"terminateGame": pb.ReqCommon,
"inputOperation": pb.ReqSelfOperation,
"inputChiPengGang": pb.ReqChiPengGang,
"confirmNewRound": pb.ReqCommon,
"broadcastInGame": pb.ReqBroadcastInGame,
"inputGameGMCommand": pb.ReqGMCommandInGaming,
"fetchGamePlayerState": pb.ReqCommon,
"checkNetworkDelay": pb.ReqCommon,
    }
    _res = {
"authGame": pb.ResAuthGame,
"enterGame": pb.ResEnterGame,
"syncGame": pb.ResSyncGame,
"finishSyncGame": pb.ResCommon,
"terminateGame": pb.ResCommon,
"inputOperation": pb.ResCommon,
"inputChiPengGang": pb.ResCommon,
"confirmNewRound": pb.ResCommon,
"broadcastInGame": pb.ResCommon,
"inputGameGMCommand": pb.ResCommon,
"fetchGamePlayerState": pb.ResGamePlayerState,
"checkNetworkDelay": pb.ResCommon,
    }

    def get_package_name(self):
        return "lq"

    def get_service_name(self):
        return "FastTest"

    def get_req_class(self, method):
        return FastTest._req[method]

    def get_res_class(self, method):
        return FastTest._res[method]


    async def authGame(self, req):
        return await self.call_method("authGame", req)


    async def enterGame(self, req):
        return await self.call_method("enterGame", req)


    async def syncGame(self, req):
        return await self.call_method("syncGame", req)


    async def finishSyncGame(self, req):
        return await self.call_method("finishSyncGame", req)


    async def terminateGame(self, req):
        return await self.call_method("terminateGame", req)


    async def inputOperation(self, req):
        return await self.call_method("inputOperation", req)


    async def inputChiPengGang(self, req):
        return await self.call_method("inputChiPengGang", req)


    async def confirmNewRound(self, req):
        return await self.call_method("confirmNewRound", req)


    async def broadcastInGame(self, req):
        return await self.call_method("broadcastInGame", req)


    async def inputGameGMCommand(self, req):
        return await self.call_method("inputGameGMCommand", req)


    async def fetchGamePlayerState(self, req):
        return await self.call_method("fetchGamePlayerState", req)


    async def checkNetworkDelay(self, req):
        return await self.call_method("checkNetworkDelay", req)

