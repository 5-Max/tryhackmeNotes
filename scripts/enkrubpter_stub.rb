require "base64"

module Enkrubpter
  class << self
    def enkrubpter(input, key)
      output = ''
      for i in 0..input.length-1
        output << (input[i].ord ^ key[i%key.length].ord)
      end
      return Base64.encode64(output)
    end

    def dekrubpter(input, key) # code for dekrubpter in lib/enkrubpter.rb, not available online.
      return input
    end
  end
end

key = 'abcd' # replace with real key when running
en = Enkrubpter::enkrubpter('test string', key)
puts en
puts Enkrubpter::dekrubpter(en, key)
