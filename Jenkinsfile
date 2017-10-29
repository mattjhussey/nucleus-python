node ('docker') {

  docker.image('python:2.7.14').inside('-u root') {
    stage 'Get tools'
      pip install tox
    
    stage 'Test'
      tox
  }
}