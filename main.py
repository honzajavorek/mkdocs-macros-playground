def define_env(env):
    env.variables['content_variable'] = 'works!'


def on_pre_page_macros(env):
    env.page.meta['content_and_template_variable'] = 'works!'
