def define_env(env):
    env.conf['content_variable'] = 123


def on_pre_page_macros(env):
    env.page.meta['content_and_template_variable'] = 456
