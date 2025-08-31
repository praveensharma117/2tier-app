pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/praveensharma117/2tier-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('backend') {
                    script {
                        docker.build("flask-backend")
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-token', url: '' ]) {
                    sh 'docker tag flask-backend devpraveens/2tier-app:latest'
                    sh 'docker push devpraveens/2tier-app:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'helm upgrade --install two-tier-app helm-chart/'
            }
        }
    }
}
