source ../.venv/bin/activate

manim-slides render main.py ThreeLayerAppScene EvolutionOfDeploymentSlide BareMetalDeployment VirtualMachineDeployment ContainersDeployment VirtualMachineVsContainer ProblemWithContainer KubernetesLogo KubernetesOverview KubernetesHowItWorks KubernetesComponent

manim-slides convert ThreeLayerAppScene EvolutionOfDeploymentSlide BareMetalDeployment VirtualMachineDeployment ContainersDeployment VirtualMachineVsContainer ProblemWithContainer KubernetesLogo KubernetesOverview KubernetesHowItWorks KubernetesComponent final_slide.html --open
