node {
  docker.image('python:2.7.14') {
    stage 'Get tools'
      pip install tox
    
    stage 'Test'
      tox
  }
}