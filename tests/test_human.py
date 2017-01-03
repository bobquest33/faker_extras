
def test_pos_attribute(fake):
    assert isinstance(fake.pos_attribute(), str)


def test_neg_attribute(fake):
    assert isinstance(fake.neg_attribute(), str)


def test_mood(fake):
    assert isinstance(fake.mood(), str)


def test_gender(fake):
    assert isinstance(fake.gender(), str)


def test_religion(fake):
    assert isinstance(fake.religion(), str)


def test_race(fake):
    assert isinstance(fake.race(), str)


def test_eye_color(fake):
    assert isinstance(fake.eye_color(), str)


def test_hair_color(fake):
    assert isinstance(fake.hair_color(), str)


def test_shirt_size(fake):
    assert isinstance(fake.shirt_size(), str)


def test_hair_style(fake):
    assert isinstance(fake.hair_style(), str)


def test_handedness(fake):
    assert isinstance(fake.handedness(), str)


def test_face_shape(fake):
    assert isinstance(fake.face_shape(), str)
