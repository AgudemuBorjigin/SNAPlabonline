import json
from .models import Response, Task


def user_next_trial(task_id, user):
    # Returns: context
    # trialnum first incomplete trial for user for given task.
    # If task completed by user, returns None

    resps_user = Response.objects.filter(subject_id=user.id)
    resps_user_task = resps_user.filter(parent_task_id=task_id)

    task = Task.objects.get(pk=task_id)
    display_name = task.displayname

    with open(task.trialinfo.path) as fp:
        info = json.load(fp)

    # Overall info
    instructions = info['instructions']
    feedback = info['feedback']

    # Get trials info from task
    trials = info['trials']
    ntrials = len(trials)

    # Get icon from task
    icon_url = task.icon.url

    done = True
    for k in range(ntrials):
        trialnum = k + 1
        if not resps_user_task.filter(trialnum=trialnum).exists():
            done = False
            break

    if done:
        trialnum = None

    # If there are more trials to be done:
    if trialnum is not None:
        k = trialnum - 1  # Python index starts at zero
        stim_url = 'stimuli/' + trials[k]['stimulus']
        prompt = trials[k]['prompt']
        choices = trials[k]['choices']
        answer = trials[k]['answer']
        progress = k * 100./ntrials
    else:
        stim_url = None
        prompt = ''
        choices = []
        answer = None
        progress = 100.

    return {'stim_url': stim_url, 'prompt': prompt,
            'instructions': instructions, 'choices': choices,
            'icon_url': icon_url, 'done': done,
            'ntrials': ntrials, 'progress': progress,
            'feedback': feedback, 'answer': answer,
            'trialnum': trialnum, 'display_name': display_name}
