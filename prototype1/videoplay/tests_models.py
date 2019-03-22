from django.test import TestCase
from videoplay.models import ScoreOneStimulus, VideoUrl,ScoreTwoStimulus
import videoplay.views as views
class ScoreOneStimulusTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        line1=ScoreOneStimulus.userScore.create(user_name="test01", session_id=1, vid_id="vid_001",score=98)
        line2=ScoreOneStimulus.userScore.create(user_name="test01", session_id=1, vid_id="vid_002",score=99)
        line3=ScoreOneStimulus.userScore.create(user_name="test02", session_id=1, vid_id="vid_003",score=58)
        line4=ScoreOneStimulus.userScore.create(user_name="test02", session_id=1, vid_id="vid_004",score=78)
        line5=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_005",score=88)
        line6=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_006")
        line6=ScoreOneStimulus.userScore.create(user_name="test01", session_id=2, vid_id="vid_007")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    def test_Score_Table_Intialization(self):
        line1=ScoreOneStimulus.userScore.get(user_name="test01", session_id=1, vid_id="vid_001")
        score=line1.score
        self.assertEqual(score, 98)
    def test_CheckUserExists_1(self):
        self.assertTrue(views.checkUserExists_1("test01"))
        self.assertFalse(views.checkUserExists_1("random"))
    def test_checkSession_1(self):
        self.assertEqual(views.checkSession_1("test01")[0],"oldsession")
        self.assertEqual(views.checkSession_1("test01")[1],["vid_006","vid_007"])
        self.assertEqual(views.checkSession_1("test02")[0],"newsession")
    def test_findSession_1(self):
        self.assertEqual(views.findSessionId_1("test01"),2)
        self.assertEqual(views.findSessionId_1("test02"),1)
    def test_incSession_1(self):
        self.assertEqual(views.incSessionId_1("test02"),2)
    def test_NewEntry_1(self):
        entrylist=views.NewEntry_1("test_new",["vid_1","vid2","vid3"])
        self.assertEqual(entrylist,["vid_1","vid2","vid3"])
    def test_updateScore_1(self):
        views.updateScore_1("test01", 2, "vid_006", 98)
        obj=ScoreOneStimulus.userScore.get(user_name="test01", session_id=2, vid_id="vid_006")
        self.assertEqual(obj.score,98)
    def test_backendlogic_1(self):
        self.assertEqual(views.backendlogic_1("test01"),["vid_006","vid_007"])
        self.assertEqual(views.backendlogic_1("test02"),views.video_lists)


    





