from invoke import task
from invoke import Responder
import target

@task
def test_response(c):
  responder = Responder(
    pattern = r"Enter your license:",
    response = "/home/test/Downloads/Foglight.license\n",
  )

  c.run("python3.7 target.py", watchers=[responder])

