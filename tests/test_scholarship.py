
import pytest

from ScholarshipEligibilityEvaluator import evaluate_scholarship, Status


def test_approved():
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.APPROVED
    assert r.reasons == [
        "Applicant meets all scholarship requirements."
    ]


def test_manual_review():
    r = evaluate_scholarship(
        age=17,
        gpa=8.0,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.MANUAL_REVIEW
    assert r.reasons == [
        "Applicant is under 18 and requires manual review."
    ]


def test_low_gpa():
    r = evaluate_scholarship(
        age=18,
        gpa=5.9,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "GPA is below the minimum required."
    ]


def test_low_attendance():
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=74.9,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "Attendance rate is below the minimum required."
    ]


def test_missing_courses():
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=90.0,
        has_required_courses=False,
        disciplinary_record=False
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "Required courses have not been completed."
    ]


def test_disciplinary_record():
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=True
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "Applicant has a disciplinary record."
    ]


@pytest.mark.parametrize(
    "age, status, reason",
    [
        (
            15,
            Status.REJECTED,
            "Applicant is younger than the minimum age."
        ),
        (
            16,
            Status.MANUAL_REVIEW,
            "Applicant is under 18 and requires manual review."
        ),
        (
            17,
            Status.MANUAL_REVIEW,
            "Applicant is under 18 and requires manual review."
        ),
        (
            18,
            Status.APPROVED,
            "Applicant meets all scholarship requirements."
        ),
    ]
)
def test_age_limits(age, status, reason):
    r = evaluate_scholarship(
        age=age,
        gpa=8.0,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == status
    assert r.reasons == [reason]


@pytest.mark.parametrize(
    "gpa, status, reason",
    [
        (
            5.99,
            Status.REJECTED,
            "GPA is below the minimum required."
        ),
        (
            6.0,
            Status.MANUAL_REVIEW,
            "GPA is in the manual review range."
        ),
        (
            6.99,
            Status.MANUAL_REVIEW,
            "GPA is in the manual review range."
        ),
        (
            7.0,
            Status.APPROVED,
            "Applicant meets all scholarship requirements."
        ),
    ]
)
def test_gpa_limits(gpa, status, reason):
    r = evaluate_scholarship(
        age=18,
        gpa=gpa,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == status
    assert r.reasons == [reason]


@pytest.mark.parametrize(
    "att, status, reason",
    [
        (
            74.99,
            Status.REJECTED,
            "Attendance rate is below the minimum required."
        ),
        (
            75.0,
            Status.MANUAL_REVIEW,
            "Attendance rate is in the manual review range."
        ),
        (
            79.99,
            Status.MANUAL_REVIEW,
            "Attendance rate is in the manual review range."
        ),
        (
            80.0,
            Status.APPROVED,
            "Applicant meets all scholarship requirements."
        ),
    ]
)
def test_attendance_limits(att, status, reason):
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=att,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == status
    assert r.reasons == [reason]


@pytest.mark.parametrize("gpa", [-0.01, 10.01])
def test_invalid_gpa(gpa):
    with pytest.raises(
        ValueError,
        match="GPA must be between 0 and 10."
    ):
        evaluate_scholarship(
            age=18,
            gpa=gpa,
            attendance_rate=90.0,
            has_required_courses=True,
            disciplinary_record=False
        )


@pytest.mark.parametrize("att", [-0.01, 100.01])
def test_invalid_attendance(att):
    with pytest.raises(
        ValueError,
        match="Attendance rate must be between 0 and 100."
    ):
        evaluate_scholarship(
            age=18,
            gpa=8.0,
            attendance_rate=att,
            has_required_courses=True,
            disciplinary_record=False
        )


def test_gpa_zero_is_valid():
    r = evaluate_scholarship(
        age=18,
        gpa=0.0,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "GPA is below the minimum required."
    ]


def test_gpa_ten_is_valid():
    r = evaluate_scholarship(
        age=18,
        gpa=10.0,
        attendance_rate=90.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.APPROVED
    assert r.reasons == [
        "Applicant meets all scholarship requirements."
    ]


def test_attendance_zero_is_valid():
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=0.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "Attendance rate is below the minimum required."
    ]


def test_attendance_hundred_is_valid():
    r = evaluate_scholarship(
        age=18,
        gpa=8.0,
        attendance_rate=100.0,
        has_required_courses=True,
        disciplinary_record=False
    )

    assert r.status == Status.APPROVED
    assert r.reasons == [
        "Applicant meets all scholarship requirements."
    ]


def test_rejection_over_review():
    r = evaluate_scholarship(
        age=17,
        gpa=6.5,
        attendance_rate=77.0,
        has_required_courses=False,
        disciplinary_record=False
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "Required courses have not been completed."
    ]


def test_multiple_rejections():
    r = evaluate_scholarship(
        age=15,
        gpa=5.5,
        attendance_rate=70.0,
        has_required_courses=False,
        disciplinary_record=True
    )

    assert r.status == Status.REJECTED
    assert r.reasons == [
        "Applicant is younger than the minimum age.",
        "GPA is below the minimum required.",
        "Attendance rate is below the minimum required.",
        "Required courses have not been completed.",
        "Applicant has a disciplinary record."
    ]


def test_invalid_gpa_error_message():
    with pytest.raises(ValueError) as e:
        evaluate_scholarship(
            age=18,
            gpa=-1.0,
            attendance_rate=90.0,
            has_required_courses=True,
            disciplinary_record=False
        )

    assert str(e.value) == "GPA must be between 0 and 10."


def test_invalid_attendance_error_message():
    with pytest.raises(ValueError) as e:
        evaluate_scholarship(
            age=18,
            gpa=8.0,
            attendance_rate=-1.0,
            has_required_courses=True,
            disciplinary_record=False
        )

    assert str(e.value) == "Attendance rate must be between 0 and 100."
