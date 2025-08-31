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
                        docker.build("flask-backend", ".")
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', '2tier-app') {
                        sh "docker tag flask-backend devpraveens/2tire-app:latest"
                        sh "docker push devpraveens/2tire-app:latest"
                    }
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
