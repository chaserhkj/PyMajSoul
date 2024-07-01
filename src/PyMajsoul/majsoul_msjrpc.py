
from . import majsoul_pb2 as pb
from .msjrpc import MSJRpcService



class Lobby(MSJRpcService):
    _req = {
"fetchConnectionInfo": pb.ReqCommon,
"fetchQueueInfo": pb.ReqCommon,
"cancelQueue": pb.ReqCommon,
"openidCheck": pb.ReqOpenidCheck,
"signup": pb.ReqSignupAccount,
"login": pb.ReqLogin,
"fetchInfo": pb.ReqCommon,
"loginSuccess": pb.ReqCommon,
"emailLogin": pb.ReqEmailLogin,
"oauth2Auth": pb.ReqOauth2Auth,
"oauth2Check": pb.ReqOauth2Check,
"oauth2Signup": pb.ReqOauth2Signup,
"oauth2Login": pb.ReqOauth2Login,
"dmmPreLogin": pb.ReqDMMPreLogin,
"createPhoneVerifyCode": pb.ReqCreatePhoneVerifyCode,
"createEmailVerifyCode": pb.ReqCreateEmailVerifyCode,
"verfifyCodeForSecure": pb.ReqVerifyCodeForSecure,
"bindPhoneNumber": pb.ReqBindPhoneNumber,
"unbindPhoneNumber": pb.ReqUnbindPhoneNumber,
"fetchPhoneLoginBind": pb.ReqCommon,
"createPhoneLoginBind": pb.ReqCreatePhoneLoginBind,
"bindEmail": pb.ReqBindEmail,
"modifyPassword": pb.ReqModifyPassword,
"bindAccount": pb.ReqBindAccount,
"logout": pb.ReqLogout,
"heatbeat": pb.ReqHeatBeat,
"loginBeat": pb.ReqLoginBeat,
"createNickname": pb.ReqCreateNickname,
"modifyNickname": pb.ReqModifyNickname,
"modifyBirthday": pb.ReqModifyBirthday,
"fetchRoom": pb.ReqCommon,
"fetchGamingInfo": pb.ReqCommon,
"createRoom": pb.ReqCreateRoom,
"joinRoom": pb.ReqJoinRoom,
"leaveRoom": pb.ReqCommon,
"readyPlay": pb.ReqRoomReady,
"dressingStatus": pb.ReqRoomDressing,
"startRoom": pb.ReqRoomStart,
"kickPlayer": pb.ReqRoomKick,
"modifyRoom": pb.ReqModifyRoom,
"matchGame": pb.ReqJoinMatchQueue,
"cancelMatch": pb.ReqCancelMatchQueue,
"fetchAccountInfo": pb.ReqAccountInfo,
"changeAvatar": pb.ReqChangeAvatar,
"receiveVersionReward": pb.ReqCommon,
"fetchAccountStatisticInfo": pb.ReqAccountStatisticInfo,
"fetchAccountChallengeRankInfo": pb.ReqAccountInfo,
"fetchAccountCharacterInfo": pb.ReqCommon,
"shopPurchase": pb.ReqShopPurchase,
"fetchGameRecord": pb.ReqGameRecord,
"readGameRecord": pb.ReqGameRecord,
"fetchGameRecordList": pb.ReqGameRecordList,
"fetchCollectedGameRecordList": pb.ReqCommon,
"fetchGameRecordsDetail": pb.ReqGameRecordsDetail,
"addCollectedGameRecord": pb.ReqAddCollectedGameRecord,
"removeCollectedGameRecord": pb.ReqRemoveCollectedGameRecord,
"changeCollectedGameRecordRemarks": pb.ReqChangeCollectedGameRecordRemarks,
"fetchLevelLeaderboard": pb.ReqLevelLeaderboard,
"fetchChallengeLeaderboard": pb.ReqChallangeLeaderboard,
"fetchMutiChallengeLevel": pb.ReqMutiChallengeLevel,
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
"openAllRewardItem": pb.ReqOpenAllRewardItem,
"composeShard": pb.ReqComposeShard,
"fetchAnnouncement": pb.ReqFetchAnnouncement,
"readAnnouncement": pb.ReqReadAnnouncement,
"fetchMailInfo": pb.ReqCommon,
"readMail": pb.ReqReadMail,
"deleteMail": pb.ReqDeleteMail,
"takeAttachmentFromMail": pb.ReqTakeAttachment,
"receiveAchievementReward": pb.ReqReceiveAchievementReward,
"receiveAchievementGroupReward": pb.ReqReceiveAchievementGroupReward,
"fetchAchievementRate": pb.ReqCommon,
"fetchAchievement": pb.ReqCommon,
"buyShiLian": pb.ReqBuyShiLian,
"matchShiLian": pb.ReqCommon,
"goNextShiLian": pb.ReqCommon,
"updateClientValue": pb.ReqUpdateClientValue,
"fetchClientValue": pb.ReqCommon,
"clientMessage": pb.ReqClientMessage,
"fetchCurrentMatchInfo": pb.ReqCurrentMatchInfo,
"userComplain": pb.ReqUserComplain,
"fetchReviveCoinInfo": pb.ReqCommon,
"gainReviveCoin": pb.ReqCommon,
"fetchDailyTask": pb.ReqCommon,
"refreshDailyTask": pb.ReqRefreshDailyTask,
"useGiftCode": pb.ReqUseGiftCode,
"useSpecialGiftCode": pb.ReqUseGiftCode,
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
"cancelGooglePlayOrder": pb.ReqCancelGooglePlayOrder,
"openChest": pb.ReqOpenChest,
"buyFromChestShop": pb.ReqBuyFromChestShop,
"fetchDailySignInInfo": pb.ReqCommon,
"doDailySignIn": pb.ReqCommon,
"doActivitySignIn": pb.ReqDoActivitySignIn,
"fetchCharacterInfo": pb.ReqCommon,
"updateCharacterSort": pb.ReqUpdateCharacterSort,
"changeMainCharacter": pb.ReqChangeMainCharacter,
"changeCharacterSkin": pb.ReqChangeCharacterSkin,
"changeCharacterView": pb.ReqChangeCharacterView,
"setHiddenCharacter": pb.ReqSetHiddenCharacter,
"sendGiftToCharacter": pb.ReqSendGiftToCharacter,
"sellItem": pb.ReqSellItem,
"fetchCommonView": pb.ReqCommon,
"changeCommonView": pb.ReqChangeCommonView,
"saveCommonViews": pb.ReqSaveCommonViews,
"fetchCommonViews": pb.ReqCommonViews,
"fetchAllCommonViews": pb.ReqCommon,
"useCommonView": pb.ReqUseCommonView,
"upgradeCharacter": pb.ReqUpgradeCharacter,
"addFinishedEnding": pb.ReqFinishedEnding,
"receiveEndingReward": pb.ReqFinishedEnding,
"gameMasterCommand": pb.ReqGMCommand,
"fetchShopInfo": pb.ReqCommon,
"buyFromShop": pb.ReqBuyFromShop,
"buyFromZHP": pb.ReqBuyFromZHP,
"refreshZHPShop": pb.ReqReshZHPShop,
"fetchMonthTicketInfo": pb.ReqCommon,
"payMonthTicket": pb.ReqCommon,
"exchangeCurrency": pb.ReqExchangeCurrency,
"exchangeChestStone": pb.ReqExchangeCurrency,
"exchangeDiamond": pb.ReqExchangeCurrency,
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
"createJPWebMoneyOrder": pb.ReqCreateJPWebMoneyOrder,
"createJPSoftbankOrder": pb.ReqCreateJPSoftbankOrder,
"createJPPayPayOrder": pb.ReqCreateJPPayPayOrder,
"fetchJPCommonCreditCardOrder": pb.ReqFetchJPCommonCreditCardOrder,
"createJPGMOOrder": pb.ReqCreateJPGMOOrder,
"createENPaypalOrder": pb.ReqCreateENPaypalOrder,
"createENMasterCardOrder": pb.ReqCreateENMasterCardOrder,
"createENVisaOrder": pb.ReqCreateENVisaOrder,
"createENJCBOrder": pb.ReqCreateENJCBOrder,
"createENAlipayOrder": pb.ReqCreateENAlipayOrder,
"createKRPaypalOrder": pb.ReqCreateKRPaypalOrder,
"createKRMasterCardOrder": pb.ReqCreateKRMasterCardOrder,
"createKRVisaOrder": pb.ReqCreateKRVisaOrder,
"createKRJCBOrder": pb.ReqCreateKRJCBOrder,
"createKRAlipayOrder": pb.ReqCreateKRAlipayOrder,
"createDMMOrder": pb.ReqCreateDMMOrder,
"createIAPOrder": pb.ReqCreateIAPOrder,
"createSteamOrder": pb.ReqCreateSteamOrder,
"verifySteamOrder": pb.ReqVerifySteamOrder,
"createMyCardAndroidOrder": pb.ReqCreateMyCardOrder,
"createMyCardWebOrder": pb.ReqCreateMyCardOrder,
"createPaypalOrder": pb.ReqCreatePaypalOrder,
"createXsollaOrder": pb.ReqCreateXsollaOrder,
"verifyMyCardOrder": pb.ReqVerifyMyCardOrder,
"verificationIAPOrder": pb.ReqVerificationIAPOrder,
"createYostarSDKOrder": pb.ReqCreateYostarOrder,
"createBillingOrder": pb.ReqCreateBillingOrder,
"solveGooglePlayOrder": pb.ReqSolveGooglePlayOrder,
"solveGooglePayOrderV3": pb.ReqSolveGooglePlayOrderV3,
"deliverAA32Order": pb.ReqDeliverAA32Order,
"fetchMisc": pb.ReqCommon,
"modifySignature": pb.ReqModifySignature,
"fetchIDCardInfo": pb.ReqCommon,
"updateIDCardInfo": pb.ReqUpdateIDCardInfo,
"fetchVipReward": pb.ReqCommon,
"gainVipReward": pb.ReqGainVipReward,
"fetchRefundOrder": pb.ReqCommon,
"fetchCustomizedContestList": pb.ReqFetchCustomizedContestList,
"fetchCustomizedContestExtendInfo": pb.ReqFetchCustomizedContestExtendInfo,
"fetchCustomizedContestAuthInfo": pb.ReqFetchCustomizedContestAuthInfo,
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
"completeActivityFlipTask": pb.ReqCompleteActivityTask,
"completePeriodActivityTask": pb.ReqCompleteActivityTask,
"completePeriodActivityTaskBatch": pb.ReqCompletePeriodActivityTaskBatch,
"completeRandomActivityTask": pb.ReqCompleteActivityTask,
"receiveActivityFlipTask": pb.ReqReceiveActivityFlipTask,
"completeSegmentTaskReward": pb.ReqCompleteSegmentTaskReward,
"fetchActivityFlipInfo": pb.ReqFetchActivityFlipInfo,
"gainAccumulatedPointActivityReward": pb.ReqGainAccumulatedPointActivityReward,
"gainMultiPointActivityReward": pb.ReqGainMultiPointActivityReward,
"fetchRankPointLeaderboard": pb.ReqFetchRankPointLeaderboard,
"gainRankPointReward": pb.ReqGainRankPointReward,
"richmanActivityNextMove": pb.ReqRichmanNextMove,
"richmanAcitivitySpecialMove": pb.ReqRichmanSpecialMove,
"richmanActivityChestInfo": pb.ReqRichmanChestInfo,
"createGameObserveAuth": pb.ReqCreateGameObserveAuth,
"refreshGameObserveAuth": pb.ReqRefreshGameObserveAuth,
"fetchActivityBuff": pb.ReqCommon,
"upgradeActivityBuff": pb.ReqUpgradeActivityBuff,
"upgradeActivityLevel": pb.ReqUpgradeActivityLevel,
"receiveUpgradeActivityReward": pb.ReqReceiveUpgradeActivityReward,
"upgradeChallenge": pb.ReqCommon,
"refreshChallenge": pb.ReqCommon,
"fetchChallengeInfo": pb.ReqCommon,
"forceCompleteChallengeTask": pb.ReqForceCompleteChallengeTask,
"fetchChallengeSeason": pb.ReqCommon,
"receiveChallengeRankReward": pb.ReqReceiveChallengeRankReward,
"fetchABMatchInfo": pb.ReqCommon,
"buyInABMatch": pb.ReqBuyInABMatch,
"receiveABMatchReward": pb.ReqCommon,
"quitABMatch": pb.ReqCommon,
"startUnifiedMatch": pb.ReqStartUnifiedMatch,
"cancelUnifiedMatch": pb.ReqCancelUnifiedMatch,
"fetchGamePointRank": pb.ReqGamePointRank,
"fetchSelfGamePointRank": pb.ReqGamePointRank,
"readSNS": pb.ReqReadSNS,
"replySNS": pb.ReqReplySNS,
"likeSNS": pb.ReqLikeSNS,
"digMine": pb.ReqDigMine,
"fetchLastPrivacy": pb.ReqFetchLastPrivacy,
"checkPrivacy": pb.ReqCheckPrivacy,
"responseCaptcha": pb.ReqResponseCaptcha,
"fetchRPGBattleHistory": pb.ReqFetchRPGBattleHistory,
"fetchRPGBattleHistoryV2": pb.ReqFetchRPGBattleHistory,
"receiveRPGRewards": pb.ReqReceiveRPGRewards,
"receiveRPGReward": pb.ReqReceiveRPGReward,
"buyArenaTicket": pb.ReqBuyArenaTicket,
"enterArena": pb.ReqEnterArena,
"receiveArenaReward": pb.ReqArenaReward,
"fetchOBToken": pb.ReqFetchOBToken,
"receiveCharacterRewards": pb.ReqReceiveCharacterRewards,
"feedActivityFeed": pb.ReqFeedActivityFeed,
"sendActivityGiftToFriend": pb.ReqSendActivityGiftToFriend,
"receiveActivityGift": pb.ReqReceiveActivityGift,
"receiveAllActivityGift": pb.ReqReceiveAllActivityGift,
"fetchFriendGiftActivityData": pb.ReqFetchFriendGiftActivityData,
"openPreChestItem": pb.ReqOpenPreChestItem,
"fetchVoteActivity": pb.ReqFetchVoteActivity,
"voteActivity": pb.ReqVoteActivity,
"unlockActivitySpot": pb.ReqUnlockActivitySpot,
"unlockActivitySpotEnding": pb.ReqUnlockActivitySpotEnding,
"receiveActivitySpotReward": pb.ReqReceiveActivitySpotReward,
"deleteAccount": pb.ReqCommon,
"cancelDeleteAccount": pb.ReqCommon,
"logReport": pb.ReqLogReport,
"bindOauth2": pb.ReqBindOauth2,
"fetchOauth2Info": pb.ReqFetchOauth2,
"setLoadingImage": pb.ReqSetLoadingImage,
"fetchShopInterval": pb.ReqCommon,
"fetchActivityInterval": pb.ReqCommon,
"fetchRecentFriend": pb.ReqCommon,
"openGacha": pb.ReqOpenGacha,
"taskRequest": pb.ReqTaskRequest,
"simulationActivityTrain": pb.ReqSimulationActivityTrain,
"fetchSimulationGameRecord": pb.ReqFetchSimulationGameRecord,
"startSimulationActivityGame": pb.ReqStartSimulationActivityGame,
"fetchSimulationGameRank": pb.ReqFetchSimulationGameRank,
"generateCombiningCraft": pb.ReqGenerateCombiningCraft,
"moveCombiningCraft": pb.ReqMoveCombiningCraft,
"combiningRecycleCraft": pb.ReqCombiningRecycleCraft,
"recoverCombiningRecycle": pb.ReqRecoverCombiningRecycle,
"finishCombiningOrder": pb.ReqFinishCombiningOrder,
"upgradeVillageBuilding": pb.ReqUpgradeVillageBuilding,
"receiveVillageBuildingReward": pb.ReqReceiveVillageBuildingReward,
"startVillageTrip": pb.ReqStartVillageTrip,
"receiveVillageTripReward": pb.ReqReceiveVillageTripReward,
"completeVillageTask": pb.ReqCompleteVillageTask,
"getFriendVillageData": pb.ReqGetFriendVillageData,
"setVillageWorker": pb.ReqSetVillageWorker,
"nextRoundVillage": pb.ReqNextRoundVillage,
"resolveFestivalActivityProposal": pb.ReqResolveFestivalActivityProposal,
"resolveFestivalActivityEvent": pb.ReqResolveFestivalActivityEvent,
"buyFestivalProposal": pb.ReqBuyFestivalProposal,
    }
    _res = {
"fetchConnectionInfo": pb.ResConnectionInfo,
"fetchQueueInfo": pb.ResFetchQueueInfo,
"cancelQueue": pb.ResCommon,
"openidCheck": pb.ResOauth2Check,
"signup": pb.ResSignupAccount,
"login": pb.ResLogin,
"fetchInfo": pb.ResFetchInfo,
"loginSuccess": pb.ResCommon,
"emailLogin": pb.ResLogin,
"oauth2Auth": pb.ResOauth2Auth,
"oauth2Check": pb.ResOauth2Check,
"oauth2Signup": pb.ResOauth2Signup,
"oauth2Login": pb.ResLogin,
"dmmPreLogin": pb.ResDMMPreLogin,
"createPhoneVerifyCode": pb.ResCommon,
"createEmailVerifyCode": pb.ResCommon,
"verfifyCodeForSecure": pb.ResVerfiyCodeForSecure,
"bindPhoneNumber": pb.ResCommon,
"unbindPhoneNumber": pb.ResCommon,
"fetchPhoneLoginBind": pb.ResFetchPhoneLoginBind,
"createPhoneLoginBind": pb.ResCommon,
"bindEmail": pb.ResCommon,
"modifyPassword": pb.ResCommon,
"bindAccount": pb.ResCommon,
"logout": pb.ResLogout,
"heatbeat": pb.ResCommon,
"loginBeat": pb.ResCommon,
"createNickname": pb.ResCommon,
"modifyNickname": pb.ResCommon,
"modifyBirthday": pb.ResCommon,
"fetchRoom": pb.ResSelfRoom,
"fetchGamingInfo": pb.ResFetchGamingInfo,
"createRoom": pb.ResCreateRoom,
"joinRoom": pb.ResJoinRoom,
"leaveRoom": pb.ResCommon,
"readyPlay": pb.ResCommon,
"dressingStatus": pb.ResCommon,
"startRoom": pb.ResCommon,
"kickPlayer": pb.ResCommon,
"modifyRoom": pb.ResCommon,
"matchGame": pb.ResCommon,
"cancelMatch": pb.ResCommon,
"fetchAccountInfo": pb.ResAccountInfo,
"changeAvatar": pb.ResCommon,
"receiveVersionReward": pb.ResCommon,
"fetchAccountStatisticInfo": pb.ResAccountStatisticInfo,
"fetchAccountChallengeRankInfo": pb.ResAccountChallengeRankInfo,
"fetchAccountCharacterInfo": pb.ResAccountCharacterInfo,
"shopPurchase": pb.ResShopPurchase,
"fetchGameRecord": pb.ResGameRecord,
"readGameRecord": pb.ResCommon,
"fetchGameRecordList": pb.ResGameRecordList,
"fetchCollectedGameRecordList": pb.ResCollectedGameRecordList,
"fetchGameRecordsDetail": pb.ResGameRecordsDetail,
"addCollectedGameRecord": pb.ResAddCollectedGameRecord,
"removeCollectedGameRecord": pb.ResRemoveCollectedGameRecord,
"changeCollectedGameRecordRemarks": pb.ResChangeCollectedGameRecordRemarks,
"fetchLevelLeaderboard": pb.ResLevelLeaderboard,
"fetchChallengeLeaderboard": pb.ResChallengeLeaderboard,
"fetchMutiChallengeLevel": pb.ResMutiChallengeLevel,
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
"openAllRewardItem": pb.ResOpenAllRewardItem,
"composeShard": pb.ResCommon,
"fetchAnnouncement": pb.ResAnnouncement,
"readAnnouncement": pb.ResCommon,
"fetchMailInfo": pb.ResMailInfo,
"readMail": pb.ResCommon,
"deleteMail": pb.ResCommon,
"takeAttachmentFromMail": pb.ResCommon,
"receiveAchievementReward": pb.ResReceiveAchievementReward,
"receiveAchievementGroupReward": pb.ResReceiveAchievementGroupReward,
"fetchAchievementRate": pb.ResFetchAchievementRate,
"fetchAchievement": pb.ResAchievement,
"buyShiLian": pb.ResCommon,
"matchShiLian": pb.ResCommon,
"goNextShiLian": pb.ResCommon,
"updateClientValue": pb.ResCommon,
"fetchClientValue": pb.ResClientValue,
"clientMessage": pb.ResCommon,
"fetchCurrentMatchInfo": pb.ResCurrentMatchInfo,
"userComplain": pb.ResCommon,
"fetchReviveCoinInfo": pb.ResReviveCoinInfo,
"gainReviveCoin": pb.ResCommon,
"fetchDailyTask": pb.ResDailyTask,
"refreshDailyTask": pb.ResRefreshDailyTask,
"useGiftCode": pb.ResUseGiftCode,
"useSpecialGiftCode": pb.ResUseSpecialGiftCode,
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
"cancelGooglePlayOrder": pb.ResCommon,
"openChest": pb.ResOpenChest,
"buyFromChestShop": pb.ResBuyFromChestShop,
"fetchDailySignInInfo": pb.ResDailySignInInfo,
"doDailySignIn": pb.ResCommon,
"doActivitySignIn": pb.ResDoActivitySignIn,
"fetchCharacterInfo": pb.ResCharacterInfo,
"updateCharacterSort": pb.ResCommon,
"changeMainCharacter": pb.ResCommon,
"changeCharacterSkin": pb.ResCommon,
"changeCharacterView": pb.ResCommon,
"setHiddenCharacter": pb.ResSetHiddenCharacter,
"sendGiftToCharacter": pb.ResSendGiftToCharacter,
"sellItem": pb.ResCommon,
"fetchCommonView": pb.ResCommonView,
"changeCommonView": pb.ResCommon,
"saveCommonViews": pb.ResCommon,
"fetchCommonViews": pb.ResCommonViews,
"fetchAllCommonViews": pb.ResAllcommonViews,
"useCommonView": pb.ResCommon,
"upgradeCharacter": pb.ResUpgradeCharacter,
"addFinishedEnding": pb.ResCommon,
"receiveEndingReward": pb.ResCommon,
"gameMasterCommand": pb.ResCommon,
"fetchShopInfo": pb.ResShopInfo,
"buyFromShop": pb.ResBuyFromShop,
"buyFromZHP": pb.ResCommon,
"refreshZHPShop": pb.ResRefreshZHPShop,
"fetchMonthTicketInfo": pb.ResMonthTicketInfo,
"payMonthTicket": pb.ResPayMonthTicket,
"exchangeCurrency": pb.ResCommon,
"exchangeChestStone": pb.ResCommon,
"exchangeDiamond": pb.ResCommon,
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
"createJPWebMoneyOrder": pb.ResCreateJPWebMoneyOrder,
"createJPSoftbankOrder": pb.ResCreateJPSoftbankOrder,
"createJPPayPayOrder": pb.ResCreateJPPayPayOrder,
"fetchJPCommonCreditCardOrder": pb.ResFetchJPCommonCreditCardOrder,
"createJPGMOOrder": pb.ResCreateJPGMOOrder,
"createENPaypalOrder": pb.ResCreateENPaypalOrder,
"createENMasterCardOrder": pb.ResCreateENMasterCardOrder,
"createENVisaOrder": pb.ResCreateENVisaOrder,
"createENJCBOrder": pb.ResCreateENJCBOrder,
"createENAlipayOrder": pb.ResCreateENAlipayOrder,
"createKRPaypalOrder": pb.ResCreateKRPaypalOrder,
"createKRMasterCardOrder": pb.ResCreateKRMasterCardOrder,
"createKRVisaOrder": pb.ResCreateKRVisaOrder,
"createKRJCBOrder": pb.ResCreateKRJCBOrder,
"createKRAlipayOrder": pb.ResCreateKRAlipayOrder,
"createDMMOrder": pb.ResCreateDmmOrder,
"createIAPOrder": pb.ResCreateIAPOrder,
"createSteamOrder": pb.ResCreateSteamOrder,
"verifySteamOrder": pb.ResCommon,
"createMyCardAndroidOrder": pb.ResCreateMyCardOrder,
"createMyCardWebOrder": pb.ResCreateMyCardOrder,
"createPaypalOrder": pb.ResCreatePaypalOrder,
"createXsollaOrder": pb.ResCreateXsollaOrder,
"verifyMyCardOrder": pb.ResCommon,
"verificationIAPOrder": pb.ResVerificationIAPOrder,
"createYostarSDKOrder": pb.ResCreateYostarOrder,
"createBillingOrder": pb.ResCreateBillingOrder,
"solveGooglePlayOrder": pb.ResCommon,
"solveGooglePayOrderV3": pb.ResCommon,
"deliverAA32Order": pb.ResCommon,
"fetchMisc": pb.ResMisc,
"modifySignature": pb.ResCommon,
"fetchIDCardInfo": pb.ResIDCardInfo,
"updateIDCardInfo": pb.ResCommon,
"fetchVipReward": pb.ResVipReward,
"gainVipReward": pb.ResCommon,
"fetchRefundOrder": pb.ResFetchRefundOrder,
"fetchCustomizedContestList": pb.ResFetchCustomizedContestList,
"fetchCustomizedContestExtendInfo": pb.ResFetchCustomizedContestExtendInfo,
"fetchCustomizedContestAuthInfo": pb.ResFetchCustomizedContestAuthInfo,
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
"completeActivityFlipTask": pb.ResCommon,
"completePeriodActivityTask": pb.ResCommon,
"completePeriodActivityTaskBatch": pb.ResCommon,
"completeRandomActivityTask": pb.ResCommon,
"receiveActivityFlipTask": pb.ResReceiveActivityFlipTask,
"completeSegmentTaskReward": pb.ResCompleteSegmentTaskReward,
"fetchActivityFlipInfo": pb.ResFetchActivityFlipInfo,
"gainAccumulatedPointActivityReward": pb.ResCommon,
"gainMultiPointActivityReward": pb.ResCommon,
"fetchRankPointLeaderboard": pb.ResFetchRankPointLeaderboard,
"gainRankPointReward": pb.ResCommon,
"richmanActivityNextMove": pb.ResRichmanNextMove,
"richmanAcitivitySpecialMove": pb.ResRichmanNextMove,
"richmanActivityChestInfo": pb.ResRichmanChestInfo,
"createGameObserveAuth": pb.ResCreateGameObserveAuth,
"refreshGameObserveAuth": pb.ResRefreshGameObserveAuth,
"fetchActivityBuff": pb.ResActivityBuff,
"upgradeActivityBuff": pb.ResActivityBuff,
"upgradeActivityLevel": pb.ResUpgradeActivityLevel,
"receiveUpgradeActivityReward": pb.ResReceiveUpgradeActivityReward,
"upgradeChallenge": pb.ResUpgradeChallenge,
"refreshChallenge": pb.ResRefreshChallenge,
"fetchChallengeInfo": pb.ResFetchChallengeInfo,
"forceCompleteChallengeTask": pb.ResCommon,
"fetchChallengeSeason": pb.ResChallengeSeasonInfo,
"receiveChallengeRankReward": pb.ResReceiveChallengeRankReward,
"fetchABMatchInfo": pb.ResFetchABMatch,
"buyInABMatch": pb.ResCommon,
"receiveABMatchReward": pb.ResCommon,
"quitABMatch": pb.ResCommon,
"startUnifiedMatch": pb.ResCommon,
"cancelUnifiedMatch": pb.ResCommon,
"fetchGamePointRank": pb.ResGamePointRank,
"fetchSelfGamePointRank": pb.ResFetchSelfGamePointRank,
"readSNS": pb.ResReadSNS,
"replySNS": pb.ResReplySNS,
"likeSNS": pb.ResLikeSNS,
"digMine": pb.ResDigMine,
"fetchLastPrivacy": pb.ResFetchLastPrivacy,
"checkPrivacy": pb.ResCommon,
"responseCaptcha": pb.ResCommon,
"fetchRPGBattleHistory": pb.ResFetchRPGBattleHistory,
"fetchRPGBattleHistoryV2": pb.ResFetchRPGBattleHistoryV2,
"receiveRPGRewards": pb.ResReceiveRPGRewards,
"receiveRPGReward": pb.ResReceiveRPGRewards,
"buyArenaTicket": pb.ResCommon,
"enterArena": pb.ResCommon,
"receiveArenaReward": pb.ResArenaReward,
"fetchOBToken": pb.ResFetchOBToken,
"receiveCharacterRewards": pb.ResReceiveCharacterRewards,
"feedActivityFeed": pb.ResFeedActivityFeed,
"sendActivityGiftToFriend": pb.ResSendActivityGiftToFriend,
"receiveActivityGift": pb.ResCommon,
"receiveAllActivityGift": pb.ResReceiveAllActivityGift,
"fetchFriendGiftActivityData": pb.ResFetchFriendGiftActivityData,
"openPreChestItem": pb.ResOpenPreChestItem,
"fetchVoteActivity": pb.ResFetchVoteActivity,
"voteActivity": pb.ResVoteActivity,
"unlockActivitySpot": pb.ResCommon,
"unlockActivitySpotEnding": pb.ResCommon,
"receiveActivitySpotReward": pb.ResReceiveActivitySpotReward,
"deleteAccount": pb.ResDeleteAccount,
"cancelDeleteAccount": pb.ResCommon,
"logReport": pb.ResCommon,
"bindOauth2": pb.ResCommon,
"fetchOauth2Info": pb.ResFetchOauth2,
"setLoadingImage": pb.ResCommon,
"fetchShopInterval": pb.ResFetchShopInterval,
"fetchActivityInterval": pb.ResFetchActivityInterval,
"fetchRecentFriend": pb.ResFetchrecentFriend,
"openGacha": pb.ResOpenGacha,
"taskRequest": pb.ResCommon,
"simulationActivityTrain": pb.ResSimulationActivityTrain,
"fetchSimulationGameRecord": pb.ResFetchSimulationGameRecord,
"startSimulationActivityGame": pb.ResStartSimulationActivityGame,
"fetchSimulationGameRank": pb.ResFetchSimulationGameRank,
"generateCombiningCraft": pb.ResGenerateCombiningCraft,
"moveCombiningCraft": pb.ResMoveCombiningCraft,
"combiningRecycleCraft": pb.ResCombiningRecycleCraft,
"recoverCombiningRecycle": pb.ResRecoverCombiningRecycle,
"finishCombiningOrder": pb.ResFinishCombiningOrder,
"upgradeVillageBuilding": pb.ResCommon,
"receiveVillageBuildingReward": pb.ResReceiveVillageBuildingReward,
"startVillageTrip": pb.ResCommon,
"receiveVillageTripReward": pb.ResReceiveVillageTripReward,
"completeVillageTask": pb.ResCompleteVillageTask,
"getFriendVillageData": pb.ResGetFriendVillageData,
"setVillageWorker": pb.ResSetVillageWorker,
"nextRoundVillage": pb.ResNextRoundVillage,
"resolveFestivalActivityProposal": pb.ResResolveFestivalActivityProposal,
"resolveFestivalActivityEvent": pb.ResResolveFestivalActivityEvent,
"buyFestivalProposal": pb.ResBuyFestivalProposal,
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


    async def fetchQueueInfo(self, req):
        return await self.call_method("fetchQueueInfo", req)


    async def cancelQueue(self, req):
        return await self.call_method("cancelQueue", req)


    async def openidCheck(self, req):
        return await self.call_method("openidCheck", req)


    async def signup(self, req):
        return await self.call_method("signup", req)


    async def login(self, req):
        return await self.call_method("login", req)


    async def fetchInfo(self, req):
        return await self.call_method("fetchInfo", req)


    async def loginSuccess(self, req):
        return await self.call_method("loginSuccess", req)


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


    async def dmmPreLogin(self, req):
        return await self.call_method("dmmPreLogin", req)


    async def createPhoneVerifyCode(self, req):
        return await self.call_method("createPhoneVerifyCode", req)


    async def createEmailVerifyCode(self, req):
        return await self.call_method("createEmailVerifyCode", req)


    async def verfifyCodeForSecure(self, req):
        return await self.call_method("verfifyCodeForSecure", req)


    async def bindPhoneNumber(self, req):
        return await self.call_method("bindPhoneNumber", req)


    async def unbindPhoneNumber(self, req):
        return await self.call_method("unbindPhoneNumber", req)


    async def fetchPhoneLoginBind(self, req):
        return await self.call_method("fetchPhoneLoginBind", req)


    async def createPhoneLoginBind(self, req):
        return await self.call_method("createPhoneLoginBind", req)


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


    async def loginBeat(self, req):
        return await self.call_method("loginBeat", req)


    async def createNickname(self, req):
        return await self.call_method("createNickname", req)


    async def modifyNickname(self, req):
        return await self.call_method("modifyNickname", req)


    async def modifyBirthday(self, req):
        return await self.call_method("modifyBirthday", req)


    async def fetchRoom(self, req):
        return await self.call_method("fetchRoom", req)


    async def fetchGamingInfo(self, req):
        return await self.call_method("fetchGamingInfo", req)


    async def createRoom(self, req):
        return await self.call_method("createRoom", req)


    async def joinRoom(self, req):
        return await self.call_method("joinRoom", req)


    async def leaveRoom(self, req):
        return await self.call_method("leaveRoom", req)


    async def readyPlay(self, req):
        return await self.call_method("readyPlay", req)


    async def dressingStatus(self, req):
        return await self.call_method("dressingStatus", req)


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


    async def receiveVersionReward(self, req):
        return await self.call_method("receiveVersionReward", req)


    async def fetchAccountStatisticInfo(self, req):
        return await self.call_method("fetchAccountStatisticInfo", req)


    async def fetchAccountChallengeRankInfo(self, req):
        return await self.call_method("fetchAccountChallengeRankInfo", req)


    async def fetchAccountCharacterInfo(self, req):
        return await self.call_method("fetchAccountCharacterInfo", req)


    async def shopPurchase(self, req):
        return await self.call_method("shopPurchase", req)


    async def fetchGameRecord(self, req):
        return await self.call_method("fetchGameRecord", req)


    async def readGameRecord(self, req):
        return await self.call_method("readGameRecord", req)


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


    async def fetchChallengeLeaderboard(self, req):
        return await self.call_method("fetchChallengeLeaderboard", req)


    async def fetchMutiChallengeLevel(self, req):
        return await self.call_method("fetchMutiChallengeLevel", req)


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


    async def openAllRewardItem(self, req):
        return await self.call_method("openAllRewardItem", req)


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


    async def receiveAchievementReward(self, req):
        return await self.call_method("receiveAchievementReward", req)


    async def receiveAchievementGroupReward(self, req):
        return await self.call_method("receiveAchievementGroupReward", req)


    async def fetchAchievementRate(self, req):
        return await self.call_method("fetchAchievementRate", req)


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


    async def userComplain(self, req):
        return await self.call_method("userComplain", req)


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


    async def useSpecialGiftCode(self, req):
        return await self.call_method("useSpecialGiftCode", req)


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


    async def doActivitySignIn(self, req):
        return await self.call_method("doActivitySignIn", req)


    async def fetchCharacterInfo(self, req):
        return await self.call_method("fetchCharacterInfo", req)


    async def updateCharacterSort(self, req):
        return await self.call_method("updateCharacterSort", req)


    async def changeMainCharacter(self, req):
        return await self.call_method("changeMainCharacter", req)


    async def changeCharacterSkin(self, req):
        return await self.call_method("changeCharacterSkin", req)


    async def changeCharacterView(self, req):
        return await self.call_method("changeCharacterView", req)


    async def setHiddenCharacter(self, req):
        return await self.call_method("setHiddenCharacter", req)


    async def sendGiftToCharacter(self, req):
        return await self.call_method("sendGiftToCharacter", req)


    async def sellItem(self, req):
        return await self.call_method("sellItem", req)


    async def fetchCommonView(self, req):
        return await self.call_method("fetchCommonView", req)


    async def changeCommonView(self, req):
        return await self.call_method("changeCommonView", req)


    async def saveCommonViews(self, req):
        return await self.call_method("saveCommonViews", req)


    async def fetchCommonViews(self, req):
        return await self.call_method("fetchCommonViews", req)


    async def fetchAllCommonViews(self, req):
        return await self.call_method("fetchAllCommonViews", req)


    async def useCommonView(self, req):
        return await self.call_method("useCommonView", req)


    async def upgradeCharacter(self, req):
        return await self.call_method("upgradeCharacter", req)


    async def addFinishedEnding(self, req):
        return await self.call_method("addFinishedEnding", req)


    async def receiveEndingReward(self, req):
        return await self.call_method("receiveEndingReward", req)


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


    async def fetchMonthTicketInfo(self, req):
        return await self.call_method("fetchMonthTicketInfo", req)


    async def payMonthTicket(self, req):
        return await self.call_method("payMonthTicket", req)


    async def exchangeCurrency(self, req):
        return await self.call_method("exchangeCurrency", req)


    async def exchangeChestStone(self, req):
        return await self.call_method("exchangeChestStone", req)


    async def exchangeDiamond(self, req):
        return await self.call_method("exchangeDiamond", req)


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


    async def createJPWebMoneyOrder(self, req):
        return await self.call_method("createJPWebMoneyOrder", req)


    async def createJPSoftbankOrder(self, req):
        return await self.call_method("createJPSoftbankOrder", req)


    async def createJPPayPayOrder(self, req):
        return await self.call_method("createJPPayPayOrder", req)


    async def fetchJPCommonCreditCardOrder(self, req):
        return await self.call_method("fetchJPCommonCreditCardOrder", req)


    async def createJPGMOOrder(self, req):
        return await self.call_method("createJPGMOOrder", req)


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


    async def createKRPaypalOrder(self, req):
        return await self.call_method("createKRPaypalOrder", req)


    async def createKRMasterCardOrder(self, req):
        return await self.call_method("createKRMasterCardOrder", req)


    async def createKRVisaOrder(self, req):
        return await self.call_method("createKRVisaOrder", req)


    async def createKRJCBOrder(self, req):
        return await self.call_method("createKRJCBOrder", req)


    async def createKRAlipayOrder(self, req):
        return await self.call_method("createKRAlipayOrder", req)


    async def createDMMOrder(self, req):
        return await self.call_method("createDMMOrder", req)


    async def createIAPOrder(self, req):
        return await self.call_method("createIAPOrder", req)


    async def createSteamOrder(self, req):
        return await self.call_method("createSteamOrder", req)


    async def verifySteamOrder(self, req):
        return await self.call_method("verifySteamOrder", req)


    async def createMyCardAndroidOrder(self, req):
        return await self.call_method("createMyCardAndroidOrder", req)


    async def createMyCardWebOrder(self, req):
        return await self.call_method("createMyCardWebOrder", req)


    async def createPaypalOrder(self, req):
        return await self.call_method("createPaypalOrder", req)


    async def createXsollaOrder(self, req):
        return await self.call_method("createXsollaOrder", req)


    async def verifyMyCardOrder(self, req):
        return await self.call_method("verifyMyCardOrder", req)


    async def verificationIAPOrder(self, req):
        return await self.call_method("verificationIAPOrder", req)


    async def createYostarSDKOrder(self, req):
        return await self.call_method("createYostarSDKOrder", req)


    async def createBillingOrder(self, req):
        return await self.call_method("createBillingOrder", req)


    async def solveGooglePlayOrder(self, req):
        return await self.call_method("solveGooglePlayOrder", req)


    async def solveGooglePayOrderV3(self, req):
        return await self.call_method("solveGooglePayOrderV3", req)


    async def deliverAA32Order(self, req):
        return await self.call_method("deliverAA32Order", req)


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


    async def fetchRefundOrder(self, req):
        return await self.call_method("fetchRefundOrder", req)


    async def fetchCustomizedContestList(self, req):
        return await self.call_method("fetchCustomizedContestList", req)


    async def fetchCustomizedContestExtendInfo(self, req):
        return await self.call_method("fetchCustomizedContestExtendInfo", req)


    async def fetchCustomizedContestAuthInfo(self, req):
        return await self.call_method("fetchCustomizedContestAuthInfo", req)


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


    async def completeActivityFlipTask(self, req):
        return await self.call_method("completeActivityFlipTask", req)


    async def completePeriodActivityTask(self, req):
        return await self.call_method("completePeriodActivityTask", req)


    async def completePeriodActivityTaskBatch(self, req):
        return await self.call_method("completePeriodActivityTaskBatch", req)


    async def completeRandomActivityTask(self, req):
        return await self.call_method("completeRandomActivityTask", req)


    async def receiveActivityFlipTask(self, req):
        return await self.call_method("receiveActivityFlipTask", req)


    async def completeSegmentTaskReward(self, req):
        return await self.call_method("completeSegmentTaskReward", req)


    async def fetchActivityFlipInfo(self, req):
        return await self.call_method("fetchActivityFlipInfo", req)


    async def gainAccumulatedPointActivityReward(self, req):
        return await self.call_method("gainAccumulatedPointActivityReward", req)


    async def gainMultiPointActivityReward(self, req):
        return await self.call_method("gainMultiPointActivityReward", req)


    async def fetchRankPointLeaderboard(self, req):
        return await self.call_method("fetchRankPointLeaderboard", req)


    async def gainRankPointReward(self, req):
        return await self.call_method("gainRankPointReward", req)


    async def richmanActivityNextMove(self, req):
        return await self.call_method("richmanActivityNextMove", req)


    async def richmanAcitivitySpecialMove(self, req):
        return await self.call_method("richmanAcitivitySpecialMove", req)


    async def richmanActivityChestInfo(self, req):
        return await self.call_method("richmanActivityChestInfo", req)


    async def createGameObserveAuth(self, req):
        return await self.call_method("createGameObserveAuth", req)


    async def refreshGameObserveAuth(self, req):
        return await self.call_method("refreshGameObserveAuth", req)


    async def fetchActivityBuff(self, req):
        return await self.call_method("fetchActivityBuff", req)


    async def upgradeActivityBuff(self, req):
        return await self.call_method("upgradeActivityBuff", req)


    async def upgradeActivityLevel(self, req):
        return await self.call_method("upgradeActivityLevel", req)


    async def receiveUpgradeActivityReward(self, req):
        return await self.call_method("receiveUpgradeActivityReward", req)


    async def upgradeChallenge(self, req):
        return await self.call_method("upgradeChallenge", req)


    async def refreshChallenge(self, req):
        return await self.call_method("refreshChallenge", req)


    async def fetchChallengeInfo(self, req):
        return await self.call_method("fetchChallengeInfo", req)


    async def forceCompleteChallengeTask(self, req):
        return await self.call_method("forceCompleteChallengeTask", req)


    async def fetchChallengeSeason(self, req):
        return await self.call_method("fetchChallengeSeason", req)


    async def receiveChallengeRankReward(self, req):
        return await self.call_method("receiveChallengeRankReward", req)


    async def fetchABMatchInfo(self, req):
        return await self.call_method("fetchABMatchInfo", req)


    async def buyInABMatch(self, req):
        return await self.call_method("buyInABMatch", req)


    async def receiveABMatchReward(self, req):
        return await self.call_method("receiveABMatchReward", req)


    async def quitABMatch(self, req):
        return await self.call_method("quitABMatch", req)


    async def startUnifiedMatch(self, req):
        return await self.call_method("startUnifiedMatch", req)


    async def cancelUnifiedMatch(self, req):
        return await self.call_method("cancelUnifiedMatch", req)


    async def fetchGamePointRank(self, req):
        return await self.call_method("fetchGamePointRank", req)


    async def fetchSelfGamePointRank(self, req):
        return await self.call_method("fetchSelfGamePointRank", req)


    async def readSNS(self, req):
        return await self.call_method("readSNS", req)


    async def replySNS(self, req):
        return await self.call_method("replySNS", req)


    async def likeSNS(self, req):
        return await self.call_method("likeSNS", req)


    async def digMine(self, req):
        return await self.call_method("digMine", req)


    async def fetchLastPrivacy(self, req):
        return await self.call_method("fetchLastPrivacy", req)


    async def checkPrivacy(self, req):
        return await self.call_method("checkPrivacy", req)


    async def responseCaptcha(self, req):
        return await self.call_method("responseCaptcha", req)


    async def fetchRPGBattleHistory(self, req):
        return await self.call_method("fetchRPGBattleHistory", req)


    async def fetchRPGBattleHistoryV2(self, req):
        return await self.call_method("fetchRPGBattleHistoryV2", req)


    async def receiveRPGRewards(self, req):
        return await self.call_method("receiveRPGRewards", req)


    async def receiveRPGReward(self, req):
        return await self.call_method("receiveRPGReward", req)


    async def buyArenaTicket(self, req):
        return await self.call_method("buyArenaTicket", req)


    async def enterArena(self, req):
        return await self.call_method("enterArena", req)


    async def receiveArenaReward(self, req):
        return await self.call_method("receiveArenaReward", req)


    async def fetchOBToken(self, req):
        return await self.call_method("fetchOBToken", req)


    async def receiveCharacterRewards(self, req):
        return await self.call_method("receiveCharacterRewards", req)


    async def feedActivityFeed(self, req):
        return await self.call_method("feedActivityFeed", req)


    async def sendActivityGiftToFriend(self, req):
        return await self.call_method("sendActivityGiftToFriend", req)


    async def receiveActivityGift(self, req):
        return await self.call_method("receiveActivityGift", req)


    async def receiveAllActivityGift(self, req):
        return await self.call_method("receiveAllActivityGift", req)


    async def fetchFriendGiftActivityData(self, req):
        return await self.call_method("fetchFriendGiftActivityData", req)


    async def openPreChestItem(self, req):
        return await self.call_method("openPreChestItem", req)


    async def fetchVoteActivity(self, req):
        return await self.call_method("fetchVoteActivity", req)


    async def voteActivity(self, req):
        return await self.call_method("voteActivity", req)


    async def unlockActivitySpot(self, req):
        return await self.call_method("unlockActivitySpot", req)


    async def unlockActivitySpotEnding(self, req):
        return await self.call_method("unlockActivitySpotEnding", req)


    async def receiveActivitySpotReward(self, req):
        return await self.call_method("receiveActivitySpotReward", req)


    async def deleteAccount(self, req):
        return await self.call_method("deleteAccount", req)


    async def cancelDeleteAccount(self, req):
        return await self.call_method("cancelDeleteAccount", req)


    async def logReport(self, req):
        return await self.call_method("logReport", req)


    async def bindOauth2(self, req):
        return await self.call_method("bindOauth2", req)


    async def fetchOauth2Info(self, req):
        return await self.call_method("fetchOauth2Info", req)


    async def setLoadingImage(self, req):
        return await self.call_method("setLoadingImage", req)


    async def fetchShopInterval(self, req):
        return await self.call_method("fetchShopInterval", req)


    async def fetchActivityInterval(self, req):
        return await self.call_method("fetchActivityInterval", req)


    async def fetchRecentFriend(self, req):
        return await self.call_method("fetchRecentFriend", req)


    async def openGacha(self, req):
        return await self.call_method("openGacha", req)


    async def taskRequest(self, req):
        return await self.call_method("taskRequest", req)


    async def simulationActivityTrain(self, req):
        return await self.call_method("simulationActivityTrain", req)


    async def fetchSimulationGameRecord(self, req):
        return await self.call_method("fetchSimulationGameRecord", req)


    async def startSimulationActivityGame(self, req):
        return await self.call_method("startSimulationActivityGame", req)


    async def fetchSimulationGameRank(self, req):
        return await self.call_method("fetchSimulationGameRank", req)


    async def generateCombiningCraft(self, req):
        return await self.call_method("generateCombiningCraft", req)


    async def moveCombiningCraft(self, req):
        return await self.call_method("moveCombiningCraft", req)


    async def combiningRecycleCraft(self, req):
        return await self.call_method("combiningRecycleCraft", req)


    async def recoverCombiningRecycle(self, req):
        return await self.call_method("recoverCombiningRecycle", req)


    async def finishCombiningOrder(self, req):
        return await self.call_method("finishCombiningOrder", req)


    async def upgradeVillageBuilding(self, req):
        return await self.call_method("upgradeVillageBuilding", req)


    async def receiveVillageBuildingReward(self, req):
        return await self.call_method("receiveVillageBuildingReward", req)


    async def startVillageTrip(self, req):
        return await self.call_method("startVillageTrip", req)


    async def receiveVillageTripReward(self, req):
        return await self.call_method("receiveVillageTripReward", req)


    async def completeVillageTask(self, req):
        return await self.call_method("completeVillageTask", req)


    async def getFriendVillageData(self, req):
        return await self.call_method("getFriendVillageData", req)


    async def setVillageWorker(self, req):
        return await self.call_method("setVillageWorker", req)


    async def nextRoundVillage(self, req):
        return await self.call_method("nextRoundVillage", req)


    async def resolveFestivalActivityProposal(self, req):
        return await self.call_method("resolveFestivalActivityProposal", req)


    async def resolveFestivalActivityEvent(self, req):
        return await self.call_method("resolveFestivalActivityEvent", req)


    async def buyFestivalProposal(self, req):
        return await self.call_method("buyFestivalProposal", req)




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
"clearLeaving": pb.ReqCommon,
"voteGameEnd": pb.ReqVoteGameEnd,
"authObserve": pb.ReqAuthObserve,
"startObserve": pb.ReqCommon,
"stopObserve": pb.ReqCommon,
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
"clearLeaving": pb.ResCommon,
"voteGameEnd": pb.ResGameEndVote,
"authObserve": pb.ResCommon,
"startObserve": pb.ResStartObserve,
"stopObserve": pb.ResCommon,
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


    async def clearLeaving(self, req):
        return await self.call_method("clearLeaving", req)


    async def voteGameEnd(self, req):
        return await self.call_method("voteGameEnd", req)


    async def authObserve(self, req):
        return await self.call_method("authObserve", req)


    async def startObserve(self, req):
        return await self.call_method("startObserve", req)


    async def stopObserve(self, req):
        return await self.call_method("stopObserve", req)

