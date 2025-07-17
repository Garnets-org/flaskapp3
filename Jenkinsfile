pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
        APP_ENV = 'production'
    }

    stages {
        stage('Trigger Parent Pipeline') {
            steps {
                script {
                    def repoUrl = env.GIT_URL
                    def repoName = repoUrl.split('/').last().replace('.git', '')
                    def shortCommit = env.GIT_COMMIT.take(7)
                    def imageName = "taye97/${repoName}:${BUILD_NUMBER}-${shortCommit}"

                    build job: 'base-pipeline',
                    parameters: [
                        string(name: 'REPO_URL', value: repoUrl),
                        string(name: 'DOCKER_IMAGE', value: imageName),
                        string(name: 'DOCKER_CREDENTIALS_ID', value: DOCKER_CREDENTIALS_ID),
                        string(name: 'APP_ENV', value: APP_ENV)
                    ]
                }
            }
        }
    }
}

