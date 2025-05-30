pipeline {
    agent any
    environment { // Corrected spelling
        DOCKER_HUB_REPO = "myatkaung/mlops-project9"
        DOCKER_HUB_CREDENTIALS_ID = "mlops-project9_docker"
    } // Added missing closing brace for environment

    stages {
        stage('Checkout Github') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-project9', url: 'https://github.com/MyatKaung/MLOPS_Project_9.git']])
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    // Use env. to access environment variables
                    dockerImage = docker.build("${env.DOCKER_HUB_REPO}:latest")
                }
            }
        }
        stage('Push Image to DockerHub') {
            steps {
                script {
                    echo 'Pushing Docker image to DockerHub...'
                    // Use env. for credentials ID and pass directly
                    docker.withRegistry('https://registry.hub.docker.com', env.DOCKER_HUB_CREDENTIALS_ID) {
                        dockerImage.push("latest") // You can also push with the full tag: dockerImage.push("${env.DOCKER_HUB_REPO}:latest")
                                               // or just dockerImage.push() if the tag was included in docker.build() and is the one you want for 'latest'
                                               // For clarity, pushing "latest" is fine if that's your intent for the 'latest' tag on Docker Hub.
                    }
                }
            }
        }
        stage('Install Kubectl & ArgoCD CLI SETUP') {
            steps {
                echo 'Installing Kubectl and ArgoCD CLI...'
                // Add actual installation commands here, e.g., using sh ''' ... '''
                sh '''
                echo 'installing Kubectl & ArgoCD cli...'
                curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                chmod +x kubectl
                mv kubectl /usr/local/bin/kubectl
                curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
                chmod +x /usr/local/bin/argocd

                '''

            }
        }
        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                echo 'Applying Kubernetes and syncing with ArgoCD...'
                // Add actual kubectl apply and argocd sync commands here
                script {
                    kubeconfig(credentialsId: 'kubeconfig', serverUrl: 'https://192.168.49.2:8443') {
                        sh '''
                        argocd login 34.16.44.218:31392 --username admin --password $(kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d) --insecure
                        argocd app sync mlopsproject9
                        '''

                       
   
}

                }

            }
        }
    }
}
