import torch
import torchvision.models as models
# define the model
model = models.mobilenet_v2(pretrained=True)
model.eval()
# trace model with a dummy input
traced_model = torch.jit.trace(model, torch.randn(1,3,224,224))
traced_model.save('model')