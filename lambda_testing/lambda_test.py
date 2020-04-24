import logging

def print_dict(dict_in, depth=0):
  paren_spacing = 2*' '*(depth-1)
  spacing = 2*' '*depth
  for key, value in dict_in.items():
    if type(value) == dict:
      print("{}'{}':\n  {}".format(paren_spacing, key, "{"))
      print_dict(value, depth+1)
      print(",{}{}".format(paren_spacing, "}"), end='')
    else:
      print("{}'{}':'{}',".format(spacing, str(key), str(value)))
  print("{}{}".format(paren_spacing, "}"))


def my_handler(event, context):

  if type(event) == dict:
    print_dict(event)
  else:
    print(str(event))
    
  logging.basicConfig(filename='example.log',level=logging.DEBUG)
  logging.info(str(context))

  message = "Hello world!"

  return {
          'message' : message
  }


if __name__ == "__main__":
    #import testpkg
    from testpkg.sampleevent import sample_event

    #print(str(sample_event))
    #print(type(sample_event))
    context_obj = {"name": "MyContextObject", "type": "ContextObjectObviously"}
    my_handler(sample_event, context_obj)
