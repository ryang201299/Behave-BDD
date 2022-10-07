pipeline {
    agent any
    stages {
        stage('Building...') {
            when {
                branch "main"
            }
            steps {
                bat "python account.py"
            }
        }
        stage('Testing...') {
            steps {
                bat 'behave'
            }
        }
    }
}