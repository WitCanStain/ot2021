from invoke import task

@task
def start(ctx, s=None, l=None):
    cmd = None
    if s:
        cmd = "python3 src/main.py" + f" s={s}"
    elif l:
        cmd = "python3 src/main.py" + f" l={l}"
    else:
        cmd = "python3 src/main.py"
    ctx.run(cmd)


@task
def test(ctx):
    ctx.run("pytest src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")