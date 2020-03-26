import model


def test():
    assert 2 > 1


def test_dk():
    m = model.Model()
    assert m.dk(10, 10) == (10, 0)
    assert m.dk(3, 0) == (1.5, 25)
    assert m.dk(3, -3) == (0, 50)
    assert m.dk(-10, -10) == (-10, 0)


def test_ik():
    m = model.Model()
    assert m.ik(10, 0) == (10, 10)
    assert m.ik(1.5, 25) == (3, 0)
    assert m.ik(0, 50) == (3, -3)
    assert m.ik(-10, 0) == (-10, -10)


def test_update_x():
    m = model.Model()
    m.m2.speed = 60
    m.m1.speed = 60
    m.update(1/60)
    assert (m.x, m.y) == (1, 0)


def test_update_rot():
    m = model.Model()
    m.m1.speed = 10
    m.m2.speed = -10
    m.update(1/60)
    assert (m.x, m.y) == (0, 0)


def test_update_diag():
    m = model.Model()
    m.m1.speed = 1
    m.m2.speed = -1
    m.update(1)
    m.m1.speed = 1
    m.m2.speed = 1
    m.update(1)
    assert (round(m.x, 2), round(m.y, 2)) == (-0.57, -0.82)
