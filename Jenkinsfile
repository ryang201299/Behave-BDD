pipeline {
    agent any
    stages {
        stage('Building...') {
            steps {
                bat "docker build -t dock_practice:0.0.1 ."
                bat "docker run dock_practice:0.0.1"
            }
        }
        stage('Testing...') {
            steps {
                bat 'behave'
            }
        }
    }
}
