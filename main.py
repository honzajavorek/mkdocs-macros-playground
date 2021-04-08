dynamic_extra_var = 'works!'

def define_env(env):
    env.variables['dynamic_macros_var'] = 'works!'
    env.variables['dynamic_extra_var'] = dynamic_extra_var


def on_pre_page_macros(env):
    env.conf['extra']['dynamic_extra_var'] = dynamic_extra_var
    env.page.meta['dynamic_meta_var'] = 'works!'
