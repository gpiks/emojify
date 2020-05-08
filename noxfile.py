import nox


@nox.session(reuse_venv=True)
def lint_check(session):
    session.install(".[lint]")
    session.run("make", "lint-check", external=True)


@nox.session()
def test_with_coverage(session):
    session.install(".[test]")
    session.run("pytest", external=True)
